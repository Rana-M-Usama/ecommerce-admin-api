# E-commerce Admin API

A FastAPI-based backend API for e-commerce administration, providing endpoints for sales analysis, inventory management, and product operations. Built with Python, FastAPI, SQLAlchemy, and SQLite.

## Project Structure
```
├── api/
│   ├── inventory.py    # Inventory management endpoints
│   ├── product.py      # Product registration endpoints
│   └── sale.py         # Sales and revenue endpoints
├── dependencies/
│   ├── database.py     # Database configuration
│   ├── deps.py         # Dependency injection
│   └── schemas.py      # Pydantic models
├── models/
│   ├── inventory.py    # Inventory ORM model
│   ├── product.py      # Product ORM model
│   └── sale.py         # Sale ORM model
└── services/
    ├── inventory_service.py    # Inventory business logic
    ├── product_service.py      # Product business logic
    └── sales_service.py        # Sales business logic
```

## API Endpoints

### Sales
- `GET /api/sales/`
  - Get filtered sales data
  - Query parameters:
    - `start_date`: Filter sales from this date
    - `end_date`: Filter sales up to this date
    - `product_id`: Filter by specific product
    - `category`: Filter by product category

- `GET /api/sales/revenue/`
  - Get revenue analysis reports
  - Query parameters:
    - `period`: Group by 'daily', 'weekly', 'monthly', or 'yearly'
    - `start_date`: Start of analysis period
    - `end_date`: End of analysis period

### Inventory
- `GET /api/inventory/`
  - Get low stock inventory items
  - Query parameters:
    - `low_stock_threshold`: Minimum stock level (default: 10)

- `PUT /api/inventory/{product_id}`
  - Update product inventory levels
  - Request body: `{"quantity": int}`

### Products
- `POST /api/products/`
  - Register new product
  - Automatically creates inventory record
  - Request body:
    ```json
    {
        "name": "string",
        "category": "string",
        "price": float
    }
    ```

## Data Models

### Product
- id: Integer (Primary Key)
- name: String
- category: String
- price: Float

### Inventory
- id: Integer (Primary Key)
- product_id: Integer (Foreign Key)
- quantity: Integer
- last_updated: DateTime

### Sale
- id: Integer (Primary Key)
- product_id: Integer (Foreign Key)
- quantity: Integer
- sale_date: DateTime
- total_amount: Float

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- SQLite 3.x

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Rana-M-Usama/ecommerce-admin-api.git
   cd ecommerce-admin-api
   ```

2. Create and activate virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  
   # or
   .venv\Scripts\activate  
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. (Optional) Load demo data:
   ```bash
   python3 demo_data.py
   ```

## API Documentation
Once the server is running, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

