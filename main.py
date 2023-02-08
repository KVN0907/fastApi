from fastapi import FastAPI, status, Response
from routers import blog_get, blog_post
from db import model
from routers import user
from db.database import engine

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {"message": "Hello World"}

model.Base.metadata.create_all(engine)

