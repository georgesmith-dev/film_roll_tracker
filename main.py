from fastapi import FastAPI
from fastapi import Path
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field
from typing import Optional

app = FastAPI()


@app.get("/")
def root():
    "Ensures the server is up"
    return {"message": "server is running"}


class Roll(BaseModel):
    "Defines the data shape of the film roll"

    stock: str = Field(min_length=3, max_length=30)
    exposures: int = Field(gt=0, lt=100)
    iso: int = Field(gt=50, lt=2000)
    developed: bool = False
    camera_used: Optional[str] = Field(min_length=1, max_length=30)




