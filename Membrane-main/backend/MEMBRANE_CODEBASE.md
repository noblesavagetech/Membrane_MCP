# Membrane Codebase

## `./fix_story_service.py`
```python
from main import get_session
from models import Story
from sqlalchemy.orm import joinedload
from services.story_service import StoryService

def get_story_fixed(self, story_id: int, user_id: int):
    return self.db.query(Story).options(joinedload(Story.chapters), joinedload(Story.characters)).filter(Story.id == story_id, Story.user_id == user_id).first()

StoryService.get_story = get_story_fixed
```

## `./main.py`
```python
import json
from typing import Optional
from fastapi import Body, Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sse_starlette.sse import EventSourceResponse
from models import BeatScene, Chapter, ChatMessage, Document, Project, User
from services.auth_service import create_access_token, get_current_user, get_password_hash, verify_password
from services.database_service import get_session, init_db
from services.file_service import create_file_record, delete_file_record, list_project_files, read_file_content, save_uploaded_file
from services.openrouter_service import MODEL_OPTIONS, openrouter_service
from services.story_service import StoryService
from services.vector_service import add_memory, search_memory

app = FastAPI(title="Membrane + Story Engine")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# Request Models
class ProjectCreateRequest(BaseModel):
    name: str = "Untitled Project"
    description: str = ""

class DocumentUpdateRequest(BaseModel):
    content: str

class StoryCreateRequest(BaseModel):
    title: str
    genre: str = ""
    premise: str = ""

class StoryUpdateRequest(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    premise: Optional[str] = None

class ChapterCreateRequest(BaseModel):
    title: str = "Untitled Chapter"

class ChapterUpdateRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None

class CharacterCreateRequest(BaseModel):
    name: str
    role: str = ""
    traits: str = ""
    backstory: str = ""
    description: str = ""

class BeatCreateRequest(BaseModel):
    story_id: int
    title: str = ""
    content: str = ""
    beat_type: str = "scene"

class WorldbuildingCreateRequest(BaseModel):
    story_id: int
    name: str
    element_type: str = "location"
    description: str = ""

class KeyEventCreateRequest(BaseModel):
    story_id: int
    title: str
    description: str = ""

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
    return service.create_story(user.id, payload.title, payload.genre, payload.premise)

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
    if payload.content: chapter.content = payload.content
    if payload.summary: chapter.summary = payload.summary
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

# Beats, Worldbuilding, KeyEvents, Generate endpoints... (same pattern)

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
    else:
        result = await service.generate_prose(chapter, story, story.characters, chapter.beats, chapter.key_events, chapter.worldbuilding, payload.prompt, payload.model)
    return {"content": result}

@app.get("/api/models")
async def get_models():
    return MODEL_OPTIONS

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

# Also add these Story endpoints if missing:

@app.post("/api/stories/{story_id}/characters")
async def create_character_full(story_id: int, payload: dict, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Create a character with full details"""
    service = StoryService(db)
    character = service.create_character(
        story_id, user.id,
        payload.get("name", "Unnamed"),
        role=payload.get("role", ""),
        traits=payload.get("traits", ""),
        backstory=payload.get("backstory", ""),
        description=payload.get("description", "")
    )
    if not character:
        raise HTTPException(status_code=404, detail="Story not found")
    return character

@app.delete("/api/stories/{story_id}/characters/{character_id}")
async def delete_character_full(story_id: int, character_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Delete a character"""
    service = StoryService(db)
    if not service.delete_character(story_id, user.id, character_id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"status": "deleted"}

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

# Also add these Story endpoints if missing:

@app.post("/api/stories/{story_id}/characters")
async def create_character_full(story_id: int, payload: dict, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Create a character with full details"""
    service = StoryService(db)
    character = service.create_character(
        story_id, user.id,
        payload.get("name", "Unnamed"),
        role=payload.get("role", ""),
        traits=payload.get("traits", ""),
        backstory=payload.get("backstory", ""),
        description=payload.get("description", "")
    )
    if not character:
        raise HTTPException(status_code=404, detail="Story not found")
    return character

@app.delete("/api/stories/{story_id}/characters/{character_id}")
async def delete_character_full(story_id: int, character_id: int, user=Depends(get_current_user), db: Session = Depends(get_session)):
    """Delete a character"""
    service = StoryService(db)
    if not service.delete_character(story_id, user.id, character_id):
        raise HTTPException(status_code=404, detail="Character not found")
    return {"status": "deleted"}
```

## `./models.py`
```python
from datetime import datetime
from sqlalchemy import JSON, Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from services.database_service import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")
    stories = relationship("Story", back_populates="user", cascade="all, delete-orphan")

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, default="Untitled Project")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="projects")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
    chat_messages = relationship("ChatMessage", back_populates="project", cascade="all, delete-orphan")
    file_uploads = relationship("FileUpload", back_populates="project", cascade="all, delete-orphan")

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project = relationship("Project", back_populates="documents")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    project = relationship("Project", back_populates="chat_messages")

class FileUpload(Base):
    __tablename__ = "file_uploads"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    file_type = Column(String, default="unknown")
    train = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    project = relationship("Project", back_populates="file_uploads")

class VectorEmbedding(Base):
    __tablename__ = "vector_embeddings"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    content_hash = Column(String, index=True)
    embedding = Column(JSON)
    meta = Column("metadata", JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)

class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="Untitled Story")
    genre = Column(String, default="")
    premise = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="stories")
    chapters = relationship("Chapter", back_populates="story", cascade="all, delete-orphan")
    characters = relationship("Character", back_populates="story", cascade="all, delete-orphan")

class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="Untitled Chapter")
    content = Column(Text, default="")
    summary = Column(Text, default="")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    story = relationship("Story", back_populates="chapters")
    beats = relationship("BeatScene", back_populates="chapter", cascade="all, delete-orphan")
    worldbuilding = relationship("WorldBuildingElement", back_populates="chapter", cascade="all, delete-orphan")
    key_events = relationship("KeyEvent", back_populates="chapter", cascade="all, delete-orphan")

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, default="")
    traits = Column(Text, default="")
    backstory = Column(Text, default="")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    story = relationship("Story", back_populates="characters")

class BeatScene(Base):
    __tablename__ = "beat_scenes"
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, default="")
    content = Column(Text, default="")
    beat_type = Column(String, default="scene")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    chapter = relationship("Chapter", back_populates="beats")

class WorldBuildingElement(Base):
    __tablename__ = "world_building_elements"
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    element_type = Column(String, default="location")
    name = Column(String, nullable=False)
    description = Column(Text, default="")
    details = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)
    chapter = relationship("Chapter", back_populates="worldbuilding")

class KeyEvent(Base):
    __tablename__ = "key_events"
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, default="")
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    chapter = relationship("Chapter", back_populates="key_events")
```

## `./services/auth_service.py`
```python
import os
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User
from services.database_service import get_session

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7
security = HTTPBearer(auto_error=False)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc

async def get_current_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security), db: Session = Depends(get_session)):
    if not credentials:
        dev_user = db.query(User).filter(User.email == "dev@example.com").first()
        if dev_user:
            return dev_user
        dev_user = User(email="dev@example.com", username="dev", password_hash=get_password_hash("dev"))
        db.add(dev_user); db.commit(); db.refresh(dev_user)
        return dev_user
    payload = decode_token(credentials.credentials)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user
```

## `./services/database_service.py`
```python
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()
_engine = None
_SessionLocal = None

def get_database_url() -> str:
    database_url = os.environ.get("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        return database_url.replace("postgres://", "postgresql://", 1)
    if database_url:
        return database_url
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{data_dir / 'membrane.db'}"

def init_db():
    global _engine, _SessionLocal
    if _engine is not None:
        return _engine
    url = get_database_url()
    if url.startswith("sqlite"):
        _engine = create_engine(url, connect_args={"check_same_thread": False})
    else:
        _engine = create_engine(url)
    _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
    import models
    Base.metadata.create_all(bind=_engine)
    return _engine

def get_engine():
    if _engine is None:
        init_db()
    return _engine

def get_session():
    global _SessionLocal
    if _SessionLocal is None:
        init_db()
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## `./services/file_service.py`
```python
import os
from pathlib import Path
from typing import Optional
import aiofiles
from sqlalchemy.orm import Session
from models import FileUpload

UPLOAD_DIR = Path(os.environ.get("UPLOAD_DIR", Path(__file__).parent.parent / "data" / "uploads"))

def get_project_upload_dir(project_id: int) -> Path:
    project_dir = UPLOAD_DIR / str(project_id)
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir

async def save_uploaded_file(project_id: int, filename: str, content: bytes) -> str:
    filepath = get_project_upload_dir(project_id) / filename
    async with aiofiles.open(filepath, "wb") as f:
        await f.write(content)
    return str(filepath)

async def read_file_content(filepath: str, filename: str) -> Optional[str]:
    try:
        async with aiofiles.open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return await f.read()
    except:
        return None

def create_file_record(db: Session, project_id: int, filename: str, filepath: str, train: bool = False) -> FileUpload:
    file_type = filename.lower().split(".")[-1] if "." in filename else "unknown"
    record = FileUpload(project_id=project_id, filename=filename, filepath=filepath, file_type=file_type, train=train)
    db.add(record); db.commit(); db.refresh(record)
    return record

def list_project_files(db: Session, project_id: int):
    return db.query(FileUpload).filter(FileUpload.project_id == project_id).all()

def delete_file_record(db: Session, file_id: int, project_id: int) -> bool:
    file_record = db.query(FileUpload).filter(FileUpload.id == file_id, FileUpload.project_id == project_id).first()
    if not file_record:
        return False
    try:
        Path(file_record.filepath).unlink(missing_ok=True)
    except:
        pass
    db.delete(file_record); db.commit()
    return True
```

## `./services/openrouter_service.py`
```python
import hashlib
import json
import os
from typing import AsyncGenerator, Optional
import httpx

MODELS = {
    "default": "anthropic/claude-3.5-sonnet",
    "mini-max": "minimax/minimax-m2.5",
    "gemini-flash": "google/gemini-2.0-flash-exp",
    "deepseek": "deepseek/deepseek-v4-flash",
    "moonshot": "moonshotai/kimi-k2.5",
    "grok": "xai/grok-4-fast",
}

MODEL_OPTIONS = [
    {"id": "anthropic/claude-3.5-sonnet", "name": "Claude 3.5 Sonnet"},
    {"id": "minimax/minimax-m2.5", "name": "MiniMax M2.5"},
    {"id": "google/gemini-2.0-flash-exp", "name": "Gemini 3 Flash Preview"},
    {"id": "deepseek/deepseek-v4-flash", "name": "DeepSeek V4 Flash"},
    {"id": "moonshotai/kimi-k2.5", "name": "Kimi K2.5"},
    {"id": "xai/grok-4-fast", "name": "Grok 4.1 Fast"},
]

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

class OpenRouterService:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"

    def _get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json", "HTTP-Referer": "https://membrane.app", "X-Title": "Membrane"}

    def _resolve_model(self, model: str) -> str:
        return MODELS.get(model, model) if model != "default" else MODELS["default"]

    async def stream_chat(self, messages: list, model: str = "default", temperature: float = 0.7, max_tokens: int = 4096) -> AsyncGenerator[str, None]:
        if not self.api_key:
            yield "OpenRouter API key not configured."
            return
        payload = {"model": self._resolve_model(model), "messages": messages, "temperature": temperature, "max_tokens": max_tokens, "stream": True}
        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", f"{self.base_url}/chat/completions", headers=self._get_headers(), json=payload) as response:
                async for line in response.aiter_lines():
                    if not line.startswith("data: "):
                        continue
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                        content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        if content:
                            yield content
                    except json.JSONDecodeError:
                        continue

    async def chat(self, messages: list, model: str = "default", temperature: float = 0.7, max_tokens: int = 4096) -> str:
        if not self.api_key:
            return "OpenRouter API key not configured."
        payload = {"model": self._resolve_model(model), "messages": messages, "temperature": temperature, "max_tokens": max_tokens}
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(f"{self.base_url}/chat/completions", headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

    async def get_embedding(self, text: str) -> list:
        if not self.api_key:
            digest = hashlib.sha256(text.encode()).digest()
            return [b / 255.0 for b in digest]
        payload = {"model": "text-embedding-3-small", "input": text}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(f"{self.base_url}/embeddings", headers=self._get_headers(), json=payload)
            response.raise_for_status()
            return response.json()["data"][0]["embedding"]

    async def summarize_text(self, text: str, model: str = "default") -> str:
        return await self.chat([{"role": "system", "content": "Summarize concisely."}, {"role": "user", "content": text}], model, 0.3, 512)

openrouter_service = OpenRouterService()
```

## `./services/story_service.py`
```python
from typing import Optional
from sqlalchemy.orm import Session, joinedload
from models import BeatScene, Chapter, Character, KeyEvent, Story, WorldBuildingElement
from services.openrouter_service import openrouter_service

class StoryService:
    def __init__(self, db: Session):
        self.db = db

    def list_stories(self, user_id: int):
        return self.db.query(Story).filter(Story.user_id == user_id).all()

    def get_story(self, story_id: int, user_id: int) -> Optional[Story]:
        return self.db.query(Story).options(joinedload(Story.chapters), joinedload(Story.characters)).filter(Story.id == story_id, Story.user_id == user_id).first()

    def create_story(self, user_id: int, title: str, genre: str = "", premise: str = "") -> Story:
        story = Story(user_id=user_id, title=title, genre=genre, premise=premise)
        self.db.add(story); self.db.commit(); self.db.refresh(story)
        chapter = Chapter(story_id=story.id, title="Chapter 1", order=1)
        self.db.add(chapter); self.db.commit()
        return story

    def update_story(self, story_id: int, user_id: int, **kwargs):
        story = self.get_story(story_id, user_id)
        if story:
            for key, value in kwargs.items():
                if hasattr(story, key):
                    setattr(story, key, value)
            self.db.commit(); self.db.refresh(story)
        return story

    def delete_story(self, story_id: int, user_id: int) -> bool:
        story = self.get_story(story_id, user_id)
        if not story:
            return False
        self.db.delete(story); self.db.commit()
        return True

    def create_chapter(self, story_id: int, user_id: int, title: str = "Untitled Chapter"):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        max_order = self.db.query(Chapter).filter(Chapter.story_id == story_id).count()
        chapter = Chapter(story_id=story_id, title=title, order=max_order + 1)
        self.db.add(chapter); self.db.commit(); self.db.refresh(chapter)
        return chapter

    def list_characters(self, story_id: int, user_id: int):
        story = self.get_story(story_id, user_id)
        return story.characters if story else []

    def create_character(self, story_id: int, user_id: int, name: str, **kwargs):
        story = self.get_story(story_id, user_id)
        if not story:
            return None
        character = Character(story_id=story_id, name=name, **kwargs)
        self.db.add(character); self.db.commit(); self.db.refresh(character)
        return character

    async def summarize_chapter(self, chapter_id: int, story_id: int, user_id: int) -> Optional[str]:
        chapter = self.db.query(Chapter).filter(Chapter.id == chapter_id, Chapter.story_id == story_id).first()
        if not chapter or not chapter.content:
            return None
        summary = await openrouter_service.summarize_text(chapter.content)
        chapter.summary = summary
        self.db.commit(); self.db.refresh(chapter)
        return summary

    async def generate_prose(self, chapter: Chapter, story: Story, characters: list, beats: list, key_events: list, worldbuilding: list, prompt: str = "", model: str = "default") -> str:
        context = f"Story: {story.title}\nPremise: {story.premise}\nGenre: {story.genre}\n\nChapter: {chapter.title}"
        if chapter.summary:
            context += f"\nSummary: {chapter.summary}"
        if characters:
            context += "\n\nCharacters: " + ", ".join(f"{c.name} ({c.role})" for c in characters)
        if chapter.content:
            context += f"\n\nExisting content:\n{chapter.content}"
        messages = [{"role": "system", "content": "You are a creative writing assistant."}, {"role": "user", "content": context + f"\n\n{prompt or 'Continue the story.'}"}]
        return await openrouter_service.chat(messages, model=model)

    async def query_context(self, story_id: int, user_id: int, question: str, chapter_id: Optional[int] = None, model: str = "default") -> str:
        story = self.get_story(story_id, user_id)
        if not story:
            return "Story not found"
        context = f"Story: {story.title}\nPremise: {story.premise}"
        if story.characters:
            context += "\n\nCharacters: " + ", ".join(f"{char.name}: {char.traits}" for char in story.characters)
        chapters = sorted(story.chapters, key=lambda c: c.order)
        if chapter_id:
            chapters = [c for c in chapters if c.id == chapter_id]
        for ch in chapters:
            context += f"\n\n--- Chapter {ch.order}: {ch.title} ---"
            if ch.content:
                context += "\n" + ch.content[-2000:]
        messages = [{"role": "system", "content": "Answer based on story context."}, {"role": "user", "content": context + f"\n\nQuestion: {question}"}]
        return await openrouter_service.chat(messages, model=model)
```

## `./services/vector_service.py`
```python
import hashlib
from sqlalchemy.orm import Session
from models import VectorEmbedding
from services.openrouter_service import openrouter_service

async def add_memory(db: Session, project_id: int, content: str, metadata: dict = None) -> VectorEmbedding:
    content_hash = hashlib.sha256(content.encode()).hexdigest()
    existing = db.query(VectorEmbedding).filter(VectorEmbedding.project_id == project_id, VectorEmbedding.content_hash == content_hash).first()
    if existing:
        return existing
    embedding = await openrouter_service.get_embedding(content)
    record = VectorEmbedding(project_id=project_id, content=content, content_hash=content_hash, embedding=embedding, meta=metadata or {})
    db.add(record); db.commit(); db.refresh(record)
    return record

async def search_memory(db: Session, project_id: int, query: str, top_k: int = 10) -> list:
    query_emb = await openrouter_service.get_embedding(query)
    memories = db.query(VectorEmbedding).filter(VectorEmbedding.project_id == project_id).all()
    def cosine(a, b):
        if not a or not b:
            return 0.0
        length = min(len(a), len(b))
        dot = sum(x * y for x, y in zip(a[:length], b[:length]))
        mag = (sum(x * x for x in a[:length]) * sum(y * y for y in b[:length])) ** 0.5
        return dot / mag if mag else 0.0
    scored = [(m, cosine(query_emb, m.embedding or [])) for m in memories]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [m for m, _ in scored[:top_k]]
```

