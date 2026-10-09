from app.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, CheckConstraint
from decimal import Decimal

class User(Base):
    
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(nullable = False, unique = True, primary_key = True)
    name: Mapped[str] = mapped_column(nullable = False) 
    email: Mapped[str] = mapped_column(nullable = False, unique = True)
    password_hash: Mapped[str] = mapped_column(nullable = False)
    height: Mapped[Decimal] = mapped_column(Numeric(5, 1), nullable = False)

    __table_args__ = (
        CheckConstraint("height >= 130 AND height <= 230", name = "check_height_range"),
    )