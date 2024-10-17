from flask import Flask
from routes.customers import customers_bp
from routes.products import products_bp
from routes.orders import orders_bp

app = Flask(__name__)

# Register Blueprints for modular routes
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(orders_bp, url_prefix='/orders')

if __name__ == '__main__':
    app.run(debug=True)
