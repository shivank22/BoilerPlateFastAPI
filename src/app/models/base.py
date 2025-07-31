from sqlmodel import SQLModel, create_engine, Session
from src.app.config.loader import config

db_conf = config["database"]
DATABASE_URL = f"postgresql://{db_conf['user']}:{db_conf['password']}@{db_conf['host']}:{db_conf['port']}/{db_conf['dbname']}"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
