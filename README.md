# E-commerce Application

## Overview
Welcome to the E-commerce Application! This platform is designed to handle core e-commerce functionalities such as managing customers, products, orders, and customer accounts. Built with Flask and SQLAlchemy, this application offers a fully functional API for managing the backend operations of an e-commerce store, including product management, customer management, and order processing.

## Features
Customer Management (CRUD):
* Add, retrieve, update, and delete customers.
Customer Account Management (CRUD):
* Create, read, update, and delete customer accounts (e.g., usernames and passwords).
Product Management (CRUD):
* Manage the product catalog with functionality to add, retrieve, update, and delete products.
Order Management:
* Place new orders, retrieve order details, and view order history for customers.
Modular API Endpoints:
* Each feature is accessible via structured and RESTful API endpoints for integration with frontend or other services.

## Setup Instructions
1. Clone the repository:
```
git clone https://github.com/MatthewGUser/CT-MP_E-Commerce
cd CT-MP_E-Commerce
```
2: Create a Virtual Environment (Optional but Recommended)
Create and activate a virtual environment to manage your dependencies:
```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
3: Install Required Dependencies:
Install all necessary dependencies, which are listed in the `requirements.txt` file:
```
pip install -r requirements.txt
```
4: Database Setup:
Update the `app.config['SQLALCHEMY_DATABASE_URI']` in your `connect_to_db.py` file with your MySQL credentials:
```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<username>:<password>@localhost/<database>'```

Run database migrations to create the necessary tables:
```
flask db init
flask db migrate
flask db upgrade
```
5: Running the Application
Start the Flask application by running:
`python app.py`
The app will be available at http://127.0.0.1:5000.

## API Endpoints
### Customer Management
Create Customer: POST /customers
* Payload: { "name": "John Doe", "email": "john@example.com", "phone": "123-456-7890" }
Retrieve Customer: GET /customers/<int:id>
Update Customer: PUT /customers/<int:id>
* Payload: { "name": "John Smith", "email": "johnsmith@example.com", "phone": "987-654-3210" }
Delete Customer: DELETE /customers/<int:id>

### Customer Account Management
Create Customer Account: POST /customer_accounts
* Payload: { "username": "john_doe", "password": "securepassword", "customer_id": 1 }
Retrieve Customer Account: GET /customer_accounts/<int:id>
Update Customer Account: PUT /customer_accounts/<int:id>
* Payload: { "username": "john_updated", "password": "newpassword" }
Delete Customer Account: DELETE /customer_accounts/<int:id>

### Product Management
Create Product: POST /products
* Payload: { "name": "Product A", "price": 99.99 }
Retrieve Product: GET /products/<int:id>
Update Product: PUT /products/<int:id>
* Payload: { "name": "Product B", "price": 149.99 }
Delete Product: DELETE /products/<int:id>
List All Products: GET /products

### Order Management
Place an Order: POST /orders
* Payload: { "customer_id": 1, "items": [{ "product_id": 1, "quantity": 2 }, { "product_id": 2, "quantity": 1 }] }
Retrieve an Order: GET /orders/<int:id>
List All Orders: GET /orders

## Example Usage
### Placing an order
1. Create a customer:
```
POST /customers
Payload: { "name": "Jane Doe", "email": "jane@example.com", "phone": "555-1234" }
```
Response:
```
{ "message": "Customer created successfully" }
```
2. Add a product:
```
POST /products
Payload: { "name": "Laptop", "price": 799.99 }
```
3. Place an order:
```
POST /orders
Payload: { "customer_id": 1, "items": [{ "product_id": 1, "quantity": 2 }] }
```
4. retrieve an order:
```
GET /orders/1
```

## Data Validation and Error Handling
Ensures proper data input such as valid email formats and field presence.
Graceful error handling with meaningful messages for cases like missing fields or non-existent records.

## File Structure
Here’s the modular breakdown of the project files:
```
ecommerce_application/
├── migrations/          # Database migration files (if using Alembic)
├── routes/
│   ├── customers.py     # Routes for managing customers and customer accounts
│   ├── products.py      # Routes for managing products
│   ├── orders.py        # Routes for managing orders
├── app.py               # Main application file to start the Flask app
├── connect_to_db.py     # Database connection and initialization file
├── models.py            # Database models (Customer, Product, Order, etc.)
├── schemas.py           # Marshmallow schemas for serialization and validation
├── requirements.txt     # List of required dependencies
├── README.md            # This README file
```


## Conclusion
This E-commerce Application demonstrates fundamental concepts of building RESTful APIs using Flask and SQLAlchemy. With features like Customer and Product management and seamless Order processing, it provides a strong foundation for further development into a fully functional e-commerce platform.