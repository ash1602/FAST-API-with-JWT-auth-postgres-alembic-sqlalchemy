from sqlalchemy.sql.functions import mode
from starlette.responses import Response
from . import models
from .databases import SessionLocal, engine, get_db
from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .schemas import PostBase as Posts
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 

@app.get("/showall")
def get_post(db: Session = Depends(get_db)):
    posts = db.query(models.Post)
    print(posts)
    posts = db.query(models.Post).all()
    return {"data":posts}
    
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_post(post: Posts, db: Session = Depends(get_db)):
    # new_post = models.Post(**post.dict())
    new_post = models.Post(title=post.title, content=post.content, published = post.published)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}

@app.get("/showall/{id}")
def get_one(id : int, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    print(posts)
    if not posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Blog with this id doesnt exist")
    return {"data":posts}

@app.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, post: Posts, db: Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id)
    if not posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    posts.update(post.dict())
    db.commit()
    return {"data":posts}



@app.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    posts = db.query(models.Post).filter(models.Post.id == id)
    if not posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    posts.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
