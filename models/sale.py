from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from dependencies.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    sale_date = Column(DateTime, nullable=False, index=True)
    total_amount = Column(Float, nullable=False) 