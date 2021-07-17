from fastapi import APIRouter

router = APIRouter(
        prefix="/units",
        tags=["units"]
        )

@router.get("/")
async def read_units():
    return [{"singular name": "Cup", "plural name": "Cups", "conversions": []}]
