from . import models
from .database import engine
from fastapi import FastAPI
from .routers import blog, user,authentication
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
# origins = [
 
#     "http://localhost",
#     "http://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

