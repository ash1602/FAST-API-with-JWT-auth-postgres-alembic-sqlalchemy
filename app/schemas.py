from typing import Optional
from pydantic import BaseModel , EmailStr
from pydantic.types import NonPositiveFloat


class BlogBase(BaseModel):
    title : str
    content : str
    published : bool =True 


class ShowBlog(BaseModel):
    title : str
    content : str
    class Config():
        orm_mode = True
        
        
class UserCreate(BaseModel):
    email : EmailStr
    password : str


class Userout(BaseModel):
    id :int
    email: EmailStr
    class Config():
        orm_mode = True

class UserLogin(BaseModel):
    email :EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id: Optional[str] = None