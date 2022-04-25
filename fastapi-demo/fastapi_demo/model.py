from sqlalchemy import Column, Integer, String

from database import engine, Base

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name" , String(32))
    email = Column("email", String, unique=True)


Base.metadata.create_all(bind=engine)
