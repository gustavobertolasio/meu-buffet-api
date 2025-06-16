from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/")
def login():
    return {"Hello": "World"}
