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
