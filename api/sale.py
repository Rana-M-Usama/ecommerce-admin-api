from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional
import dependencies.schemas as schemas
from dependencies.deps import get_db
from services import sales_service

sales_router = APIRouter()

@sales_router.get("/", response_model=List[schemas.Sale])
def get_sales(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    product_id: Optional[int] = None,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Retrieve sales records with optional filtering parameters.
    
    Parameters:
    - start_date: Filter sales from this date onwards
    - end_date: Filter sales up to this date
    - product_id: Filter sales for a specific product
    - category: Filter sales by product category
    """
    return sales_service.get_filtered_sales(db, start_date, end_date, product_id, category)

@sales_router.get("/revenue/", response_model=schemas.RevenueReport)
def get_revenue(
    period: str = "daily",
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    """
    Generate a revenue report grouped by specified time period.
    
    Parameters:
    - period: Time grouping ('daily', 'weekly', 'monthly' , 'yearly')
    - start_date: Start date for the report period
    - end_date: End date for the report period
    """
    periods = sales_service.get_revenue_report(db, period, start_date, end_date)
    return {"periods": periods}