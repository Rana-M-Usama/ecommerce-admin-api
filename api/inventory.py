from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import dependencies.schemas as schemas
from dependencies.deps import get_db
from services import inventory_service

inventory_router = APIRouter()

@inventory_router.get("/", response_model=List[schemas.Inventory])
def get_inventory(
    low_stock_threshold: Optional[int] = 10,
    db: Session = Depends(get_db)
):
    """
    Retrieve inventory items with stock levels below the specified threshold.
    
    Parameters:
    - low_stock_threshold: Minimum stock level threshold (default: 10)
    """
    return inventory_service.get_low_stock_inventory(db, low_stock_threshold)

@inventory_router.put("/{product_id}", response_model=schemas.Inventory)
def update_inventory(
    product_id: int,
    inventory: schemas.InventoryUpdate,
    db: Session = Depends(get_db)
):
    """
    Update inventory levels for a specific product.
    
    Parameters:
    - product_id: ID of the product to update
    - inventory: Updated inventory information
    """
    return inventory_service.update_product_inventory(db, product_id, inventory) 