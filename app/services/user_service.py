from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import user_repository
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    def get_user(self, db: Session, user_id: int) -> User:
        user = user_repository.get(db, id=user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return user

    def get_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return user_repository.get_multi(db, skip=skip, limit=limit)

    def create_user(self, db: Session, *, user_in: UserCreate) -> User:
        user = user_repository.get_by_email(db, email=user_in.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user with this email already exists in the system.",
            )
        user = user_repository.get_by_username(db, username=user_in.username)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The user with this username already exists in the system.",
            )
        return user_repository.create(db, obj_in=user_in)

    def update_user(self, db: Session, *, user_id: int, user_in: UserUpdate) -> User:
        db_user = self.get_user(db, user_id=user_id)
        return user_repository.update(db, db_obj=db_user, obj_in=user_in)

    def delete_user(self, db: Session, *, user_id: int) -> User:
        db_user = self.get_user(db, user_id=user_id)
        return user_repository.remove(db, id=user_id)

user_service = UserService()
