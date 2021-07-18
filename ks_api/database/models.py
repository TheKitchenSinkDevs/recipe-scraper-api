from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    singular_name = Column(String, unique=True, index=True)
    plural_name = Column(String, unique=True, index=True)

class Food(Base):
    __tablename__ = "food"
    id = Column(Integer, primary_key=True, index=True)
    singular_name = Column(String, unique=True, index=True)
    plural_name = Column(String, unique=True, index=True)

    #related = relationship("Food", back_populates="related")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)

    unit = Column(Integer, ForeignKey('unit.id'))
