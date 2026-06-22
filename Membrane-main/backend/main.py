import json
from typing import Optional
from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse
from models import BeatScene, Chapter, Character, ChatMessage, Document, KeyEvent, Project, Story, User, WorldBuildingElement

load_dotenv()
from services.auth_service import create_access_token, get_current_user, get_password_hash, verify_password
from services.database_service import get_session, init_db
from services.file_service import create_file_record, delete_file_record, list_project_files, read_file_content, save_uploaded_file
from services.openrouter_service import MODEL_OPTIONS, openrouter_service
from services.story_service import StoryService
from services.vector_service import add_memory, search_memory
from mcp import router as mcp_router

app = FastAPI(title="Membrane + Story Engine")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(mcp_router)

# Request Models
class ProjectCreateRequest(BaseModel):
    name: str = "Untitled Project"
    description: str = ""

class DocumentUpdateRequest(BaseModel):
    content: str

class StoryCreateRequest(BaseModel):
    title: str
    description: str = ""

class StoryUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ChapterCreateRequest(BaseModel):
    title: str = "Untitled Chapter"

class ChapterUpdateRequest(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
    summary: Optional[str] = None

class CharacterCreateRequest(BaseModel):
    name: str
    role: str = ""
    traits: str = ""
    backstory: str = ""
    description: str = ""

class BeatCreateRequest(BaseModel):
    description: str
    order: int = 0

class BeatUpdateRequest(BaseModel):
    description: Optional[str] = None
    order: Optional[int] = None

class WorldbuildingCreateRequest(BaseModel):
    category: str
    description: str

class WorldbuildingUpdateRequest(BaseModel):
    category: Optional[str] = None
    description: Optional[str] = None

class KeyEventCreateRequest(BaseModel):
    description: str
    order: int = 0

class KeyEventUpdateRequest(BaseModel):
    description: Optional[str] = None
    order: Optional[int] = None

class CharacterUpdateRequest(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    traits: Optional[str] = None
    backstory: Optional[str] = None
    description: Optional[str] = None

class MemoryAddRequest(BaseModel):
    content: str

class MemorySearchRequest(BaseModel):
    query: str
    top_k: int = 10

class GenerateRequest(BaseModel):
    prompt: str
    story_id: int
    chapter_id: Optional[int] = None
    context_type: str = "prose"
    model: str = "default"

class CharacterGenerateRequest(BaseModel):
    story_id: int
    generation_type: str = "full_profile"  # full_profile, physical_only, personality_background, speaking_style, residency_environment
    parameters: dict = {}
    use_context: bool = True
    model: str = "default"

class WorldbuildingGenerateRequest(BaseModel):
    story_id: int
    chapter_id: int
    generation_type: str = "full_setting"  # full_setting, thorough_setting, physical_dimensions, material_composition, economic_function, sensory_data, culture_society
    parameters: dict = {}
    use_context: bool = True
    model: str = "default"

@app.on_event("startup")
async def startup():
    init_db()

def require_project(project_id: int, user_id: int, db: Session) -> Project:
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Auth
@app.post("/api/auth/signup")
async def signup(email: str = Form(...), username: str = Form(...), password: str = Form(...), db: Session = Depends(get_session)):
    existing = db.query(User).filter((User.email == email) | (User.username == username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(email=email, username=username, password_hash=get_password_hash(password))
    db.add(user); db.commit(); db.refresh(user)
    return {"token": create_access_token({"sub": str(user.id)}), "user": {"id": user.id, "email": user.email, "username": user.username}}

@app.post("/api/auth/login")
async def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_session)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": create_access_token({"sub": str(user.id)}), "user": {"id": user.id, "email": user.email, "username": user.username}}

@app.get("/api/auth/me")
async def get_me(user=Depends(get_current_user)):
    return {"id": user.id, "email": user.email, "username": user.username}

# Projects
@app.get("/api/projects")
async def list_projects(user=Depends(get_current_user), db: Session = Depends(get_session)):
    return db.query(Project).filter(Project.user_id == user.id).all()

@app.post("/api/projects")
async def create_project(payload: ProjectCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    project = Project(user_id=user.id, name=payload.name, description=payload.description)
    db.add(project); db.commit(); db.refresh(project)
    doc = Document(project_id=project.id)
    db.add(doc); db.commit()
    return project

@app.get("/api/projects/{project_id}")
async def get_project(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    return require_project(project_id, user.id, db)

@app.put("/api/projects/{project_id}")
async def update_project(project_id: int, payload: ProjectCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    project = require_project(project_id, user.id, db)
    project.name = payload.name
    project.description = payload.description
    db.commit(); db.refresh(project)
    return project

@app.delete("/api/projects/{project_id}")
async def delete_project(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    project = require_project(project_id, user.id, db)
    db.delete(project); db.commit()
    return {"status": "deleted"}

@app.get("/api/projects/{project_id}/document")
async def get_document(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.project_id == project_id).first()
    if not doc:
        doc = Document(project_id=project_id); db.add(doc); db.commit(); db.refresh(doc)
    return doc

@app.put("/api/projects/{project_id}/document")
async def update_document(project_id: int, payload: DocumentUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.project_id == project_id).first()
    if not doc:
        doc = Document(project_id=project_id); db.add(doc)
    doc.content = payload.content
    db.commit(); db.refresh(doc)
    return doc

# Chat with SSE
@app.get("/api/projects/{project_id}/chat/stream")
async def chat_stream(project_id: int, message: str, selected_text: str = "", model: str = "default", user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.project_id == project_id).first()
    doc_content = doc.content if doc else ""
    system_msg = "You are a helpful writing assistant."
    if selected_text:
        system_msg += f" Selected text: '{selected_text}'"
    chat_hist = [{"role": "system", "content": system_msg}, {"role": "user", "content": f"Document:\n{doc_content}\n\nMessage: {message}"}]
    user_msg = ChatMessage(project_id=project_id, role="user", content=message)
    db.add(user_msg); db.commit()

    async def event_generator():
        full_response = ""
        async for chunk in openrouter_service.stream_chat(chat_hist, model=model):
            full_response += chunk
            yield {"data": json.dumps({"content": chunk})}
        ai_msg = ChatMessage(project_id=project_id, role="assistant", content=full_response)
        db.add(ai_msg); db.commit()
        yield {"data": "[DONE]"}
    return EventSourceResponse(event_generator())

# File uploads
@app.post("/api/projects/{project_id}/upload/file")
async def upload_file(project_id: int, train: bool = Form(False), file: UploadFile = File(...), user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    content = await file.read()
    filepath = await save_uploaded_file(project_id, file.filename, content)
    file_record = create_file_record(db, project_id, file.filename, filepath, train)
    if train:
        text = await read_file_content(filepath, file.filename)
        if text:
            await add_memory(db, project_id, text, {"filename": file.filename})
    return file_record

@app.get("/api/projects/{project_id}/upload/list")
async def list_files(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    return list_project_files(db, project_id)

@app.delete("/api/projects/{project_id}/upload/file/{file_id}")
async def delete_file(project_id: int, file_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    if not delete_file_record(db, file_id, project_id):
        raise HTTPException(status_code=404, detail="File not found")
    return {"status": "deleted"}

# Memory
@app.post("/api/projects/{project_id}/memory/add")
async def add_to_memory(project_id: int, payload: MemoryAddRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    memory = await add_memory(db, project_id, payload.content)
    return {"id": memory.id}

@app.post("/api/projects/{project_id}/memory/search")
async def search_project_memory(project_id: int, payload: MemorySearchRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    require_project(project_id, user.id, db)
    results = await search_memory(db, project_id, payload.query, payload.top_k)
    return [{"id": r.id, "content": r.content, "metadata": r.meta} for r in results]

# Stories
@app.get("/api/stories")
async def list_stories(user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.list_stories(user.id)

@app.post("/api/stories")
async def create_story(payload: StoryCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.create_story(user.id, payload.title, payload.description)

@app.get("/api/stories/{story_id}")
async def get_story(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story = service.get_story(story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story

@app.put("/api/stories/{story_id}")
async def update_story(story_id: int, payload: StoryUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    story = service.update_story(story_id, user.id, **kwargs)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story

@app.delete("/api/stories/{story_id}")
async def delete_story(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    if not service.delete_story(story_id, user.id):
        raise HTTPException(status_code=404, detail="Story not found")
    return {"status": "deleted"}

@app.post("/api/stories/{story_id}/chapters")
async def create_chapter(story_id: int, payload: ChapterCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    chapter = service.create_chapter(story_id, user.id, payload.title)
    if not chapter:
        raise HTTPException(status_code=404, detail="Story not found")
    return chapter

@app.put("/api/chapters/{chapter_id}")
async def update_chapter(chapter_id: int, payload: ChapterUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if payload.title: chapter.title = payload.title
    if payload.text is not None: chapter.text = payload.text
    if payload.summary is not None: chapter.summary = payload.summary
    db.commit(); db.refresh(chapter)
    return chapter

@app.post("/api/chapters/{chapter_id}/summarize")
async def summarize_chapter(chapter_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    summary = await service.summarize_chapter(chapter_id, chapter.story_id, user.id)
    return {"summary": summary}

@app.get("/api/stories/{story_id}/characters")
async def list_characters(story_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    return service.list_characters(story_id, user.id)

@app.post("/api/stories/{story_id}/characters")
async def create_character(story_id: int, payload: CharacterCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    character = service.create_character(story_id, user.id, payload.name, role=payload.role, traits=payload.traits, backstory=payload.backstory, description=payload.description)
    if not character:
        raise HTTPException(status_code=404, detail="Story not found")
    return character

@app.put("/api/stories/{story_id}/characters/{character_id}")
async def update_character(story_id: int, character_id: int, payload: CharacterUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    character = service.update_character(character_id, story_id, user.id, **kwargs)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.delete("/api/stories/{story_id}/characters/{character_id}")
async def delete_character(story_id: int, character_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    if not service.delete_character(character_id, story_id, user.id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"status": "deleted"}

# Beats
@app.post("/api/chapters/{chapter_id}/beats")
async def create_beat(chapter_id: int, payload: BeatCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    beat = service.create_beat(chapter_id, payload.description, payload.order)
    return beat

@app.get("/api/chapters/{chapter_id}/beats")
async def get_beats(chapter_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return service.get_beats(chapter_id)

@app.put("/api/chapters/{chapter_id}/beats/{beat_id}")
async def update_beat(chapter_id: int, beat_id: int, payload: BeatUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    beat = service.update_beat(beat_id, **kwargs)
    if not beat:
        raise HTTPException(status_code=404, detail="Beat not found")
    return beat

@app.delete("/api/chapters/{chapter_id}/beats/{beat_id}")
async def delete_beat(chapter_id: int, beat_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if not service.delete_beat(beat_id):
        raise HTTPException(status_code=404, detail="Beat not found")
    return {"status": "deleted"}

# World Building
@app.post("/api/chapters/{chapter_id}/worldbuilding")
async def create_world_element(chapter_id: int, payload: WorldbuildingCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    elem = service.create_world_element(chapter_id, payload.category, payload.description)
    return elem

@app.get("/api/chapters/{chapter_id}/worldbuilding")
async def get_world_elements(chapter_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return service.get_world_elements(chapter_id)

@app.put("/api/chapters/{chapter_id}/worldbuilding/{element_id}")
async def update_world_element(chapter_id: int, element_id: int, payload: WorldbuildingUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    elem = service.update_world_element(element_id, **kwargs)
    if not elem:
        raise HTTPException(status_code=404, detail="World element not found")
    return elem

@app.delete("/api/chapters/{chapter_id}/worldbuilding/{element_id}")
async def delete_world_element(chapter_id: int, element_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if not service.delete_world_element(element_id):
        raise HTTPException(status_code=404, detail="World element not found")
    return {"status": "deleted"}

# Key Events
@app.post("/api/chapters/{chapter_id}/keyevents")
async def create_key_event(chapter_id: int, payload: KeyEventCreateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    event = service.create_key_event(chapter_id, payload.description, payload.order)
    return event

@app.get("/api/chapters/{chapter_id}/keyevents")
async def get_key_events(chapter_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return service.get_key_events(chapter_id)

@app.put("/api/chapters/{chapter_id}/keyevents/{event_id}")
async def update_key_event(chapter_id: int, event_id: int, payload: KeyEventUpdateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    kwargs = {k: v for k, v in payload.model_dump().items() if v is not None}
    event = service.update_key_event(event_id, **kwargs)
    if not event:
        raise HTTPException(status_code=404, detail="Key event not found")
    return event

@app.delete("/api/chapters/{chapter_id}/keyevents/{event_id}")
async def delete_key_event(chapter_id: int, event_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story_ids = [s.id for s in service.list_stories(user.id)]
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter or chapter.story_id not in story_ids:
        raise HTTPException(status_code=404, detail="Chapter not found")
    if not service.delete_key_event(event_id):
        raise HTTPException(status_code=404, detail="Key event not found")
    return {"status": "deleted"}

# AI Generation

@app.post("/api/ai/generate")
async def generate_content(payload: GenerateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story = service.get_story(payload.story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    
    chapter = None
    if payload.chapter_id:
        chapter = db.query(Chapter).filter(Chapter.id == payload.chapter_id, Chapter.story_id == payload.story_id).first()
    elif story.chapters:
        chapter = sorted(story.chapters, key=lambda c: c.order)[0]
    
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    
    if payload.context_type == "query":
        result = await service.query_context(payload.story_id, user.id, payload.prompt, payload.chapter_id, payload.model)
    elif payload.context_type in ("prose", "beat"):
        # Frontend already builds full context with only selected characters — pass prompt directly
        result = await service.generate_from_prompt(payload.prompt, payload.model)
    else:
        result = await service.generate_prose(chapter, story, story.characters, chapter.beats, chapter.key_events, chapter.worldbuilding, payload.prompt, payload.model)
    return {"content": result}

@app.get("/api/models")
async def get_models():
    return MODEL_OPTIONS

# Character Generation
@app.post("/api/stories/{story_id}/characters/generate")
async def generate_character(story_id: int, payload: CharacterGenerateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story = service.get_story(story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    result = await service.generate_character_profile(story, payload.generation_type, payload.parameters, payload.use_context, payload.model)
    return {"content": result}

# Worldbuilding Generation
@app.post("/api/stories/{story_id}/worldbuilding/generate")
async def generate_worldbuilding(story_id: int, payload: WorldbuildingGenerateRequest, user=Depends(get_current_user), db: Session = Depends(get_session)):
    service = StoryService(db)
    story = service.get_story(story_id, user.id)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    chapter = db.query(Chapter).filter(Chapter.id == payload.chapter_id, Chapter.story_id == story_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    result = await service.generate_worldbuilding_element(story, chapter, payload.generation_type, payload.parameters, payload.use_context, payload.model)
    return {"content": result}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Add to existing endpoints (after document endpoints)

@app.get("/api/projects/{project_id}/documents")
async def list_project_documents(project_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """List all documents for a project"""
    require_project(project_id, user.id, db)
    docs = db.query(Document).filter(Document.project_id == project_id).all()
    return [{"id": d.id, "title": f"Document {d.id}", "content": d.content} for d in docs]

@app.put("/api/projects/{project_id}/documents/{document_id}")
async def update_project_document(project_id: int, document_id: int, payload: dict, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Update a specific document"""
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.id == document_id, Document.project_id == project_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    if "content" in payload:
        doc.content = payload["content"]
    db.commit()
    db.refresh(doc)
    return {"id": doc.id, "title": f"Document {doc.id}", "content": doc.content}

@app.delete("/api/projects/{project_id}/documents/{document_id}")
async def delete_project_document(project_id: int, document_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Delete a specific document"""
    require_project(project_id, user.id, db)
    doc = db.query(Document).filter(Document.id == document_id, Document.project_id == project_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(doc)
    db.commit()
    return {"status": "deleted"}


# ============ STATIC FILES FOR PRODUCTION ============
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Point to the dist folder one level up (where Vite builds)
ui_dist = os.path.join(os.path.dirname(__file__), "..", "dist")

if os.path.exists(ui_dist):
    # Mount assets folder explicitly if it exists
    assets_path = os.path.join(ui_dist, "assets")
    if os.path.exists(assets_path):
        app.mount("/assets", StaticFiles(directory=assets_path), name="assets")

    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        file_path = os.path.join(ui_dist, full_path)
        index_path = os.path.join(ui_dist, "index.html")
        
        # If the requested path is a real file (like favicon.ico, robot.txt), serve it
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        
        # For everything else (SPA routing), serve index.html
        if os.path.exists(index_path):
            return FileResponse(index_path)
        
        return {"error": "Frontend build not found or index.html missing."}

