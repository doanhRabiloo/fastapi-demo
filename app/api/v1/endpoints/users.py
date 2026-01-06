from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Users"])
def get_users():
    return {"users": ["user1", "user2"]}

