from fastapi import APIRouter, FastAPI, status, Response, Depends
from enum import Enum
from typing import Optional
from routers.blog_post import required_funcationality

router = APIRouter (
    prefix='/blog',
    tags=['blog']
)

class BlogType(str,Enum):
    short = 'short'
    long = 'long'
    story ='story'

@router.get(
         '/blog/all',
         summary="Retrive All Blogs",
         description="Api to retrive all blog"
         )
def getAllBlog(page=1, page_size=10):
    return {"message": f"All {page_size} blogs in page {page}"}

@router.get('/allOptional')
def getAllBlogOptional(page=1, page_size: Optional[int]= None, req_param: dict= Depends(required_funcationality)):
    return {"message": f"All {page_size} blogs in page {page}" , "req": req_param}

@router.get(
      '/{id}/comment/{comment_id}',
      tags=['comment'],
      summary="Retrive All Blogs with Blog id and comment id")
def getCommentId(id : int, comment_id : int, valid: bool= True, username: Optional[str] =None):
    """
     Api ti retrive the comment of a blog with ID

     - **id** is Mandatory Path parameter
     - **comment_id** is Mandatory Path parameter
     - **valid** is Optional Query Param 
     - **username** is Optional Query Param
    
    """
    return {"message": f'blog_id {id}, comment_id {comment_id}, valid {valid} username {username}'}

@router.get(
        '/type/{type}',
         summary="Retrive All Blogs by type")
def blogType(type: BlogType):
    return{"messgae": f"Blog with type {type}"}

@router.get(
        '/blog/{id}', 
         status_code = status.HTTP_200_OK, 
         tags=['blog'],
         summary="Retrive All Blogs By resposne code")
def getBlog(id: int, response: Response):
    if id > 5:
     response.status_code = status.HTTP_404_NOT_FOUND
     return {"error": f"Blog with id {id} not found"}  
    else:
     response.status_code = status.HTTP_200_OK
     return{"message":f'Blog with {id} found'}



