from flask import Blueprint, request, jsonify
from models import Product
from connect_to_db import db
from marshmallow import ValidationError

products_bp = Blueprint('products_bp', __name__)

# Create Product
@products_bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({'error': 'Missing name or price in the request data'}), 400

        new_product = Product(name=data['name'], price=data['price'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Read Product by ID
@products_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    try:
        product = Product.query.get_or_404(id)
        return jsonify({'name': product.name, 'price': product.price}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update Product
@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        product = Product.query.get_or_404(id)
        data = request.get_json()
        
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            product.price = data['price']
        
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Delete Product
@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# List All Products
@products_bp.route('/products', methods=['GET'])
def list_products():
    try:
        products = Product.query.all()
        if not products:
            return jsonify({'message': 'No products available'}), 404
        
        products_list = [{'name': product.name, 'price': product.price} for product in products]
        return jsonify(products_list), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
