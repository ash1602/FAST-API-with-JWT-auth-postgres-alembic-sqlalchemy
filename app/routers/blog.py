from typing import List
from ..schemas import BlogBase as Posts
from starlette.responses import Response
from .. import models
from .. database import  get_db
from fastapi import  Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app import schemas
from ..utils import hash

router = APIRouter(tags=['Blog'])

@router.get("/showall", response_model=List[schemas.ShowBlog])
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Blog)
    print(posts)
    posts = db.query(models.Blog).all()
    return posts
    
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_post(post: Posts, db: Session = Depends(get_db)):
    # new_post = models.Post(**post.dict())
    new_post = models.Blog(title=post.title, content=post.content, published = post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/showall/{id}", response_model=schemas.ShowBlog)
def get_one(id : int, db: Session = Depends(get_db)):
    posts = db.query(models.Blog).filter(models.Blog.id == id).first()
    print(posts)
    if not posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Blog with this id doesnt exist")
    return posts

@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, post: Posts, db: Session = Depends(get_db)):
    posts = db.query(models.Blog).filter(models.Blog.id == id)
    if not posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    posts.update(post.dict())
    db.commit()
    return posts



@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    posts = db.query(models.Blog).filter(models.Blog.id == id)
    if not posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    posts.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
