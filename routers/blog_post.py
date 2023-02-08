from typing import Dict, List, Optional
from fastapi import APIRouter, Query,Path,Body
from pydantic import BaseModel
router = APIRouter(
    prefix="/blog",
    tags = ['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    no_of_comments: int
    published: Optional[bool]
    tags: List[str] =[]
    metadata: Dict[str,str] ={"key1":"val1"}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version
        }

@router.post('/new/{id}/comment')
def create_blog_new(
                blog: BlogModel, id: int, 
                comment_title: int = Query(None,
                title="Id of the comment",
                description="Create a test post",
                alias="commentTitle",
                ),
                content: str = Body(...,
                                    min_length=5, 
                                    max_length=10,
                                    regex="^[a-z\s]*$"),
                v: Optional[List[str]] = Query(None),
                comment_id: int = Path(None, gt=5, le=10)
                ):
    
    
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content":content,
        "versio":v,
        "comment_id":comment_id

        }

@router.post('/new/{id}/comment/v1')
def create_blog(blog: BlogModel, id: int, 
                comment_id: int = Query(None,
                title="Id of the comment",
                description="Create a test post",
                alias="commentId",
                deprecated=True)):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id,
        }

def required_funcationality():
    return {"message": "FAST API Implementation"}

