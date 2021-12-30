from typing import ClassVar
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.functions import now

from sqlalchemy.sql.sqltypes import TIMESTAMP
from .databases import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title =  Column(String)
    content = Column(String)
    published = Column(Boolean, server_default= "True", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")) 