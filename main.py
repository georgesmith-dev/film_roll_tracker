from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pydantic import Field
from typing import Optional

app = FastAPI()

valid_rolls = []


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
    camera_used: Optional[str] = Field(default=None, min_length=1, max_length=30)


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
        "stock": new_roll.stock,
        "exposures": new_roll.exposures,
        "iso": new_roll.iso,
        "developed": new_roll.developed,
        "camera used": new_roll.camera_used,
    }
    valid_roll["id"] = len(valid_rolls) + 1
    valid_rolls.append(valid_roll)
    return JSONResponse(status_code=201, content={"message": "new roll created", "roll_data": valid_roll})


@app.get("/rolls/all")
def get_all_rolls():
    "returns all validated rolls"
    return valid_rolls


@app.get("/rolls/{roll_id}")
def get_roll(roll_id: int = Path(gt=0, description="Id must be greater than 0")):
    "returns a roll depending on user input"
    for valid_roll in valid_rolls:
        if valid_roll.get("id") == roll_id:
            return valid_roll
    raise HTTPException(status_code=404, detail=f"Roll {roll_id} was not found")


@app.patch("/rolls/{roll_id}/develop")
def patch_roll(roll_id: int = Path(gt=0, description="Id must be greater than 0")):
    "enables user to update developed status"
    roll = get_roll(roll_id)
    if roll.get("developed"):
        return {"message": f"Roll {roll_id} has already been developed"}
    roll["developed"] = True
    return {"message": f"Roll {roll_id} has been developed", "roll": roll}
