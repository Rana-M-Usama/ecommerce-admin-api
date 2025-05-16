from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timedelta
from sqlalchemy import func
from models import Sale, Product

def get_filtered_sales(
    db: Session,
    start_date: datetime = None,
    end_date: datetime = None,
    product_id: int = None,
    category: str = None
):
    current_date = datetime.utcnow()
    if start_date and end_date and start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date cannot be greater than end date"
        )
    if end_date and end_date > current_date:
        raise HTTPException(
            status_code=400,
            detail="End date cannot be in the future"
        )

    query = db.query(Sale).join(Product)
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    if product_id:
        query = query.filter(Sale.product_id == product_id)
    if category:
        query = query.filter(Product.category == category)
    return query.all()

def get_revenue_report(
    db: Session,
    period: str = "daily",
    start_date: datetime = None,
    end_date: datetime = None
):
    if not start_date:
        start_date = datetime.utcnow() - timedelta(days=30)
    if not end_date:
        end_date = datetime.utcnow()

    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="Start date cannot be greater than end date"
        )
    if end_date > datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="End date cannot be in the future"
        )

    # First validate the period
    valid_periods = ["daily", "weekly", "monthly", "yearly"]
    if period not in valid_periods:
        raise HTTPException(status_code=400, detail="Invalid period")

    # Then create the date_trunc expression
    date_trunc = {
        "daily": func.date(Sale.sale_date),
        "weekly": func.strftime('%Y-%W', Sale.sale_date),
        "monthly": func.strftime('%Y-%m', Sale.sale_date),
        "yearly": func.strftime('%Y', Sale.sale_date)
    }[period]  # Now we can safely use dictionary access

    result = (db.query(
        date_trunc.label("period"),
        func.sum(Sale.total_amount).label("total_revenue"),
        func.sum(Sale.quantity).label("total_units")
    ).filter(
        Sale.sale_date >= start_date,
        Sale.sale_date <= end_date
    ).group_by(date_trunc).all())

    return [
        {
            "period": int(
                (
                    datetime.strptime(f"{r.period}-1", "%Y-%W-%w") if period == "weekly" else
                    datetime.strptime(f"{r.period}-01", "%Y-%m-%d") if period == "monthly" else
                    datetime.strptime(f"{r.period}-01-01", "%Y-%m-%d") if period == "yearly" else
                    datetime.strptime(str(r.period), "%Y-%m-%d")
                ).timestamp()
            ),
            "total_revenue": float(r.total_revenue or 0),
            "total_units": int(r.total_units or 0)
        }
        for r in result
    ] 