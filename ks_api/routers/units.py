from fastapi import APIRouter, Depends, HTTPException
from ..database import crud, models, schemas, get_db
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
        prefix="/units",
        tags=["units"]
        )

@router.get("/", response_model=List[schemas.Unit])
async def read_units(db = Depends(get_db)):
    return crud.get_unit(db = db, unit_id=None)

@router.post("/", response_model=schemas.Unit)
async def create_unit(unit: schemas.UnitCreate, db= Depends(get_db)):
    db_unit = crud.get_unit_by_name(db=db, name=unit.singular_name)
    if db_unit:
        raise HTTPException(status_code=400, detail="Unit already exists")
    return crud.create_unit(db=db, unit=unit)
