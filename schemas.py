from typing import Optional,List
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    description:str
    isPublished:Optional[bool]=True
    class Config:
        orm_mode=True  




class User(BaseModel):
    name:str
    email:str
    password:str


class PresentUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog] = []
    class Config:
        orm_mode=True  
    
    
class PresentBlogs(Blog):
    author:PresentUser
    class Config:
        orm_mode=True  


class Login(BaseModel):
    username:str
    password:str   



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
