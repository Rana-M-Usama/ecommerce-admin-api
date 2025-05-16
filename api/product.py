from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import dependencies.schemas as schemas
from dependencies.deps import get_db
from services import product_service

products_router = APIRouter()

@products_router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product with initial inventory.
    
    Args:
        product (schemas.ProductCreate): Product data including name, price, and other details
        db (Session): Database session dependency
        
    Returns:
        schemas.Product: Created product information
        
    Note:
        - Creates a new product in the database
        - Automatically creates an inventory record with initial quantity of 0
    """
    return product_service.create_new_product(db, product) 