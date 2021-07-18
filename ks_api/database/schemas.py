from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

class UnitBase(BaseModel):
    singular_name: str
    plural_name: str

class UnitCreate(UnitBase):
    pass

class Unit(UnitBase):
    id: int

    class Config:
        orm_mode = True

class FoodBase(BaseModel):
    singular_name: str
    plural_name: str

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int
    related: List[Food] = []

    class Config:
        orm_mode = True

class IngredientBase(BaseModel):
    quantity: int

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int
    unit: Unit

    class Config:
        orm_mode = True
