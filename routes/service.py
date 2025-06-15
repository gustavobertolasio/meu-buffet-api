from fastapi import APIRouter

router = APIRouter(prefix="/service", tags=["service"])

@router.get("/")
def read_root():
    return {"Hello": "World"}
