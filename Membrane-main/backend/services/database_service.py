import os
from pathlib import Path
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

Base = declarative_base()
_engine = None
_SessionLocal = None


def _get_first_env(*names: str) -> str:
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return ""


def _get_postgres_url_from_parts() -> str:
    host = _get_first_env("PGHOST", "POSTGRES_HOST", "DB_HOST")
    port = _get_first_env("PGPORT", "POSTGRES_PORT", "DB_PORT")
    user = _get_first_env("PGUSER", "POSTGRES_USER", "DB_USER")
    password = _get_first_env("PGPASSWORD", "POSTGRES_PASSWORD", "DB_PASSWORD")
    database = _get_first_env("PGDATABASE", "POSTGRES_DB", "DB_NAME")

    if all([host, port, user, password, database]):
        safe_user = quote_plus(user)
        safe_password = quote_plus(password)
        return f"postgresql+psycopg2://{safe_user}:{safe_password}@{host}:{port}/{database}"

    return ""

def get_database_url() -> str:
    database_url = _get_first_env("DATABASE_URL", "POSTGRES_URL", "DATABASE_PRIVATE_URL")
    if database_url and database_url.startswith("postgres://"):
        return database_url.replace("postgres://", "postgresql://", 1)
    if database_url:
        return database_url

    postgres_url = _get_postgres_url_from_parts()
    if postgres_url:
        return postgres_url

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
