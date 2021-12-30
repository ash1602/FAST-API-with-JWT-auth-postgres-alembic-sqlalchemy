from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy import Boolean, Column, Integer, String

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String)
    content = Column(String)
    published = Column(Boolean, server_default= "True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")) 


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable= False)
    email = Column(String, nullable=False, unique= True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")) 
    
    