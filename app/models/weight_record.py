from sqlalchemy import Column, Integer, Date, DateTime, Numeric, ForeignKey, Index, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class WeightRecord(Base):
    __tablename__ = "weight_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    record_date = Column(Date, nullable=False)
    weight = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # インデックス・制約定義
    __table_args__ = (
        Index('idx_weight_record_user_date', 'user_id', 'record_date'),
        Index('idx_weight_record_user_created', 'user_id', 'created_at'),
        UniqueConstraint('user_id', 'record_date', name='uq_user_record_date'),
    )

    user = relationship("User", back_populates="weight_records")

    def __repr__(self):
        return f"<WeightRecord(id={self.id}, user_id={self.user_id}, record_date={self.record_date}, weight={self.weight})>"

