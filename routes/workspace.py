from fastapi import APIRouter

router = APIRouter(prefix="/workspace", tags=["workspace"])

@router.get("/")
def read_root():
    return {"Hello": "World"}
