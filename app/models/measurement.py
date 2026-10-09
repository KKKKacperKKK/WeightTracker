from app.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Numeric, ForeignKey, Date, CheckConstraint
from datetime import date as dateDT
from decimal import Decimal

class Measurement(Base):

    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(nullable = False, unique = True, primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable = False)
    date: Mapped[dateDT] = mapped_column(Date(), nullable = False)

    weight: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable = False)
    fat: Mapped[Decimal] = mapped_column(Numeric(4,2), nullable = True)
    muscles: Mapped[Decimal] = mapped_column(Numeric(4,2), nullable = True)
    bones: Mapped[Decimal] = mapped_column(Numeric(3,2), nullable = True)
    water: Mapped[Decimal] = mapped_column(Numeric(4,2), nullable = True)

    __table_args__ = (
        CheckConstraint("weight >= 30 AND weight <= 400", name = "check_weight_range"),
        CheckConstraint("fat >= 2 AND fat <= 60", name = "check_fat_range"),
        CheckConstraint("muscles >= 15 AND muscles <= 55", name = "check_muscles_range"),
        CheckConstraint("bones >= 0.5 AND bones <= 7", name = "check_bones_range"),
        CheckConstraint("water >= 35 AND water <= 75", name = "check_water_range"),
        
    )
   