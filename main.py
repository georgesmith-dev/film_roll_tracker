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


@app.post("/rolls")
def post_new_roll(new_roll: Roll):
    "Posts a new roll"
    valid_stock = {} # I should come up with a better way to validate a new roll
    if new_roll.stock not in valid_stock:
        raise HTTPException(status_code=409, detail="Invalid roll stock")
    return ("New roll added!"), {
        "Stock": new_roll.stock,
        "Exposures": new_roll.exposures,
        "iso": new_roll.iso,
        "developed": new_roll.developed,
        "camera used": new_roll.camera_used,
    } # I need to test this in a test.py
