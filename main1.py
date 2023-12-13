from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


@app.get('/blog')
# query parameter
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'published {limit} blog from database'}
    else:
      return {"data":f"{limit} blog form database "}

@app.get('/blog/unpublished')
def unpublished():
    return {"data":"ubpublished blog"}

@app.get('/blog/{id}')
# single blog with path parameter
def singleBlog(id:int):
    return {"data":id}

class Blog(BaseModel):
    title:str
    description:str
    published:Optional[bool]=True


@app.post('/blog')
def create_blog(blog:Blog):
    return {
        'message':'blog created successfully!',
        'data':blog
    }

