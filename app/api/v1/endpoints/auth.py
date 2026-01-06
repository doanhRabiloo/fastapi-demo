from fastapi import APIRouter

router = APIRouter()

@router.get("/login", tags=["Auth"])
def login():
    return {"message": "Login"}

