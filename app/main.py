from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

# This command tells sqlalchemy to generate sql table
# it is not needed because we have alembic
#models.Base.metadata.create_all(bind=engine)


app = FastAPI()
origins = ["*"
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    # "https://www.google.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)