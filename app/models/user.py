from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=False)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    target_weight = Column(Decimal(10, 2), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    weight_records = relationship("WeightRecord", back_populates="user")
    auth_tokens = relationship("AuthToken", back_populates="user")
    password_reset_tokens = relationship("PasswordResetToken", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"