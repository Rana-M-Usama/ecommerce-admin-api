from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
import database
from models import Product, Inventory, Sale

def populate_demo_data(db: Session):
    # Sample products
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99},
        {"name": "Smartphone", "category": "Electronics", "price": 699.99},
        {"name": "Headphones", "category": "Accessories", "price": 49.99},
        {"name": "T-shirt", "category": "Clothing", "price": 19.99},
    ]

    for prod in products:
        product = Product(**prod)
        db.add(product)
        db.commit()
        db.refresh(product)
        inventory = Inventory(
            product_id=product.id,
            quantity=random.randint(50, 200),
            last_updated=datetime.utcnow()
        )
        db.add(inventory)
    
    for day in range(30):
        sale_date = datetime.utcnow() - timedelta(days=day)
        for product in db.query(Product).all():
            if random.random() > 0.7:  
                quantity = random.randint(1, 5)
                sale = Sale(
                    product_id=product.id,
                    quantity=quantity,
                    sale_date=sale_date,
                    total_amount=quantity * product.price
                )
                db.add(sale)
    db.commit()

if __name__ == "__main__":
    db = database.SessionLocal()
    try:
        populate_demo_data(db)
        print("Demo data populated successfully.")
    finally:
        db.close()