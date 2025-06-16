from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
def read_root():
    return {"Hello": "World"}
