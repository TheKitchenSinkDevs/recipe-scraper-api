from sqlalchemy.orm import Session

from typing import Optional

from . import models, schemas

def get_unit(db: Session, unit_id: Optional[int]):
    if unit_id:
        return db.query(models.Unit).filter(models.Unit.id == unit_id).first()
    else:
        return db.query(models.Unit).all()

def get_unit_by_name(db: Session, name: Optional[str]):
    singulars = db.query(models.Unit).filter(models.Unit.singular_name==name.lower()).all()
    if len(singulars) > 0:
        return singulars
    else:
        return None

def create_unit(db: Session, unit: schemas.UnitCreate):
    db_unit = models.Unit(singular_name=unit.singular_name.lower(),
            plural_name=unit.plural_name.lower())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit
