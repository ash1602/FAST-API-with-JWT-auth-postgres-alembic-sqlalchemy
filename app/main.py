from sqlalchemy.sql.functions import mode
from . import models, schemas
from .databases import SessionLocal, engine, get_db
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

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
    