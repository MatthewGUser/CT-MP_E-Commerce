from connect_to_db import db
from datetime import datetime

# Customer Model
class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)

    customer_account = db.relationship('CustomerAccount', backref='customer', lazy=True)

    def __repr__(self):
        return f'<Customer {self.name}>'

# CustomerAccount Model
class CustomerAccount(db.Model):
    __tablename__ = 'customer_accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

    def __repr__(self):
        return f'<CustomerAccount {self.username}>'

# Product Model
class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'

# Order Model
class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float, nullable=False)
    
    customer = db.relationship('Customer', backref='orders', lazy=True)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __repr__(self):
        return f'<Order {self.id} by Customer {self.customer_id}>'

# OrderItem Model
class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    
    product = db.relationship('Product', backref='order_items', lazy=True)

    def __repr__(self):
        return f'<OrderItem {self.quantity} of Product {self.product_id} in Order {self.order_id}>'