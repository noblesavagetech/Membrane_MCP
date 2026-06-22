cat << 'INNER_EOF' >> backend/main.py

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
INNER_EOF
