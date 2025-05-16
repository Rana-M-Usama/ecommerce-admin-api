from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Optional
import dependencies.schemas as schemas
import dependencies.database as database
from sqlalchemy import func, and_

from api import product, sale, inventory

app = FastAPI(title="E-commerce Admin API")

app.include_router(product.products_router, prefix="/products")
app.include_router(sale.sales_router, prefix="/sales")
app.include_router(inventory.inventory_router, prefix="/inventory")

