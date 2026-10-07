from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime

from backend.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(120), nullable=False)
    priority=Column(String(10), nullable=False, default="medium")
    done=Column(Boolean, nullable=False, default=False)
    created_at=Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))   