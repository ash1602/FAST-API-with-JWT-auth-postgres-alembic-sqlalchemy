from pydantic import BaseModel , EmailStr


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
   