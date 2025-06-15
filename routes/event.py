from fastapi import APIRouter

router = APIRouter(prefix="/event", tags=["event"])

@router.get("/")
def get_all_events():
    return {"Hello": "World"}