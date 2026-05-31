from fastapi import FastAPI
from fastapi import Path
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import Field
from typing import Optional

app = FastAPI()

valid_rolls = (
    []
)  # I need a way to add unique IDs to these entries so get_roll will work


@app.get("/")
def root():
    "ensures the server is up"
    return {"message": "server is running"}


class Roll(BaseModel):
    "defines the data shape of the film roll"

    stock: str = Field(min_length=3, max_length=30)
    exposures: int = Field(gt=0, lt=100)
    iso: int = Field(gt=50, lt=2000)
    developed: bool = False
    camera_used: Optional[str] = Field(min_length=1, max_length=30)


@app.post("/rolls")
def post_new_roll(new_roll: Roll):
    "posts a new roll"
    valid_iso = {
        200,
        400,
        800,
    }  # I think there should still be a better way to validate this
    if new_roll.iso not in valid_iso:
        raise HTTPException(status_code=409, detail="Invalid roll data")

    valid_roll = {
        "Stock": new_roll.stock,
        "Exposures": new_roll.exposures,
        "iso": new_roll.iso,
        "developed": new_roll.developed,
        "camera used": new_roll.camera_used,
    }
    valid_rolls.append(valid_roll)
    return "New roll added!"


@app.get("/rolls/all")
def get_all_rolls():
    "returns all validates rolls"
    return valid_rolls


@app.get("/rolls/{roll_id}")
def get_roll(roll_id: int = Path(gt=0, description="Id must be greater than 0")):
    "returns a roll depending on user input"
    pass


@app.patch("/rolls/{roll_id}/develop")
def patch_roll(roll_id: int = Path(gt=0, description="Id must be greater than 0")):
    "enables user to update developed status"
    pass
