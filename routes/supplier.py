from fastapi import APIRouter

router = APIRouter(prefix="/supplier", tags=["supplier"])

@router.get("/")
def read_root():
    return {"Hello": "World"}
