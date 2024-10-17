from flask import Blueprint, request, jsonify
from models import Customer, CustomerAccount
from connect_to_db import db
from marshmallow import ValidationError

customers_bp = Blueprint('customers_bp', __name__)

# Create Customer
@customers_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({'message': 'Customer created successfully'}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# Read Customer by ID
@customers_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        return jsonify({'name': customer.name, 'email': customer.email, 'phone': customer.phone}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update Customer
@customers_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        customer.name = data['name']
        customer.email = data['email']
        customer.phone = data['phone']
        db.session.commit()
        return jsonify({'message': 'Customer updated successfully'}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# Delete Customer
@customers_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message': 'Customer deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# Create Customer Account
@customers_bp.route('/customer_accounts', methods=['POST'])
def create_customer_account():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        new_account = CustomerAccount(username=data['username'], password=data['password'], customer_id=data['customer_id'])
        db.session.add(new_account)
        db.session.commit()
        return jsonify({'message': 'Customer Account created successfully'}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# Read Customer Account by ID
@customers_bp.route('/customer_accounts/<int:id>', methods=['GET'])
def get_customer_account(id):
    try:
        account = CustomerAccount.query.get_or_404(id)
        return jsonify({'username': account.username, 'customer_id': account.customer_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update Customer Account
@customers_bp.route('/customer_accounts/<int:id>', methods=['PUT'])
def update_customer_account(id):
    try:
        account = CustomerAccount.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        account.username = data['username']
        account.password = data['password']
        db.session.commit()
        return jsonify({'message': 'Customer Account updated successfully'}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# Delete Customer Account
@customers_bp.route('/customer_accounts/<int:id>', methods=['DELETE'])
def delete_customer_account(id):
    try:
        account = CustomerAccount.query.get_or_404(id)
        db.session.delete(account)
        db.session.commit()
        return jsonify({'message': 'Customer Account deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500
