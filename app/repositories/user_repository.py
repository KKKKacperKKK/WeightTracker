from decimal import Decimal

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User


def get_by_email(db: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    result = db.scalars(statement)
    return result.first()

def get_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)

def create(
        db: Session,
        name: str,
        email: str,
        password_hash: str,
        height: Decimal
) -> User:
    user = User(name=name, email=email, password_hash=password_hash, height=height)
    db.add(user)
