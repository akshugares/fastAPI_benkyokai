from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class AuthToken(Base):
    __tablename__ = "auth_tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    access_token = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    access_token_expires_in = Column(Integer, nullable=False)
    refresh_token_expires_in = Column(Integer, nullable=False)

    user = relationship("User", back_populates="auth_tokens")

    def __repr__(self):
        return f"<AuthToken(id={self.id}, user_id={self.user_id}, created_at={self.created_at})>"

