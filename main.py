from fastapi import FastAPI
app = FastAPI()
from database import engine
from routers import blog, user,auth
import models


models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)