from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name : str
 
@app.post("/item")
def created_blog(request:Item):
    return {"data" : f"blog created as name {request.name}"}

@app.get("/")
def index(limit=10, published : bool=True, sort:Optional[str]=None):
    if published :
        return {"data":{f"sharthak , {limit}"}}
    else:
        return {"data":"None"}

@app.get("/about")
def about():
    return  {"data": "about page"}

@app.get("/blog/{id}")
def show(id: int):
    return{"data":id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)