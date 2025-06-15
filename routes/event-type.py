from fastapi import APIRouter

router = APIRouter(prefix="/event-type", tags=["event-type"])

@router.get("/")
def get_all_event_types():
    return {"Hello": "World"}
