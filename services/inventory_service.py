from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from models import Inventory
from dependencies.schemas import InventoryUpdate

def get_low_stock_inventory(db: Session, low_stock_threshold: int = 10):
    if low_stock_threshold < 0:
        raise HTTPException(
            status_code=400,
            detail="Low stock threshold cannot be negative"
        )
    
    return db.query(Inventory).filter(
        Inventory.quantity >= 0,
        Inventory.quantity <= low_stock_threshold
    ).all()

def update_product_inventory(db: Session, product_id: int, inventory: InventoryUpdate):
    if inventory.quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity cannot be negative"
        )
    
    db_inventory = db.query(Inventory).filter(
        Inventory.product_id == product_id
    ).first()
    if not db_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    
    db_inventory.quantity = inventory.quantity
    db_inventory.last_updated = datetime.utcnow()
    db.commit()
    db.refresh(db_inventory)
    return db_inventory 