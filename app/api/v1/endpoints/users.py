from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.user_service import user_service

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
):
    return user_service.get_users(db, skip=skip, limit=limit)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: UserCreate,
):
    return user_service.create_user(db, user_in=user_in)

@router.get("/{user_id}", response_model=User)
def get_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
):
    return user_service.get_user(db, user_id=user_id)

@router.put("/{user_id}", response_model=User)
def update_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
    user_in: UserUpdate,
):
    return user_service.update_user(db, user_id=user_id, user_in=user_in)

@router.delete("/{user_id}", response_model=User)
def delete_user(
    *,
    db: Session = Depends(get_db),
    user_id: int,
):
    return user_service.delete_user(db, user_id=user_id)
