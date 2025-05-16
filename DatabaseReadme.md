# Database Documentation

## Overview
This document describes the database schema for the e-commerce system. The system uses SQLite as the database engine with SQLAlchemy as the ORM (Object-Relational Mapping) framework.

## Database Configuration
- Database Type: SQLite
- Database File: `ecommerce.db`
- ORM: SQLAlchemy
- Connection URL: `sqlite:///ecommerce.db`

## Schema

### Products Table
**Table Name:** `products`

This table stores the basic information about products available in the system.

| Column    | Type    | Constraints       | Description                    |
|-----------|---------|------------------|--------------------------------|
| id        | Integer | Primary Key      | Unique identifier for product  |
| name      | String  | NOT NULL         | Name of the product           |
| category  | String  | NOT NULL         | Category of the product       |
| price     | Float   | NOT NULL         | Price of the product          |

### Sales Table
**Table Name:** `sales`

This table records all sales transactions in the system.

| Column       | Type     | Constraints                | Description                    |
|-------------|----------|---------------------------|--------------------------------|
| id          | Integer  | Primary Key               | Unique identifier for sale     |
| product_id  | Integer  | Foreign Key (products.id) | Reference to the sold product  |
| quantity    | Integer  | NOT NULL                  | Quantity sold                  |
| sale_date   | DateTime | NOT NULL, Indexed         | Date and time of sale         |
| total_amount| Float    | NOT NULL                  | Total amount of the sale      |

### Inventory Table
**Table Name:** `inventory`

This table manages the current stock levels for each product.

| Column       | Type     | Constraints                | Description                    |
|-------------|----------|---------------------------|--------------------------------|
| id          | Integer  | Primary Key               | Unique identifier for entry    |
| product_id  | Integer  | Foreign Key (products.id), | Reference to the product      |
|             |          | UNIQUE                    | (One inventory per product)    |
| quantity    | Integer  | NOT NULL                  | Current stock quantity         |
| last_updated| DateTime | NOT NULL                  | Last inventory update timestamp|

## Relationships

1. **Products → Sales**: One-to-Many
   - A product can have multiple sales records
   - Each sale is associated with exactly one product through `product_id`

2. **Products → Inventory**: One-to-One
   - Each product has exactly one inventory record
   - Each inventory record belongs to exactly one product
   - Enforced by the UNIQUE constraint on `inventory.product_id`

## Indexes
- `products.id`: Primary key index
- `sales.id`: Primary key index
- `sales.sale_date`: Index for efficient date-based queries
- `inventory.id`: Primary key index

## Notes
- All tables inherit from SQLAlchemy's `Base` class
- DateTime fields use UTC timezone
- The database is configured with `check_same_thread=False` for SQLite to allow multiple threads to access it
- Tables are automatically created during initialization through the `init_db()` function 