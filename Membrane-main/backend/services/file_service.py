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
