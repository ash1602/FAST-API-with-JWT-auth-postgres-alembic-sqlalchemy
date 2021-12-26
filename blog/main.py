from fastapi import FastAPI, Depends , HTTPException
from . import schemas
from . import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import status
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

@app.post("/blog", status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "Done"
    
    
@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request:schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.update(request)
    db.commit()
    return "updated"

    
@app.get("/blog")
def showall( db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}")
def show( id, db:Session = Depends(get_db), status_code=200):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail= "Blog with this id doesnt exist")
        # response.status_code = status.HTTP_404_NOT_FOUND
    return blogs