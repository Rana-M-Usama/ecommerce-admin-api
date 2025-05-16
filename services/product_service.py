from sqlalchemy.orm import Session
from datetime import datetime
from models import Product, Inventory
import dependencies.schemas as schemas

def create_new_product(db: Session, product: schemas.ProductCreate):
    try:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.flush()
        
        db_inventory = Inventory(
            product_id=db_product.id, 
            quantity=0, 
            last_updated=datetime.utcnow()
        )
        db.add(db_inventory)
        db.commit()
        db.refresh(db_product)
        return db_product
    except Exception as e:
        db.rollback()
        raise 