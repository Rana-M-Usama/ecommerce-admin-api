from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from dependencies.database import Base

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    last_updated = Column(DateTime, nullable=False, default=datetime.utcnow) 