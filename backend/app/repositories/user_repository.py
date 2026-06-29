from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        """
        Return user by email.
        """
        statement = select(User).where(User.email == email)

        return self.db.scalar(statement)

    def get_by_id(self, user_id: int) -> User | None:
        """
        Return user by id.
        """
        statement = select(User).where(User.id == user_id)

        return self.db.scalar(statement)

    def create(self, user: User) -> User:
        """
        Save a new user.
        """
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)

        return user