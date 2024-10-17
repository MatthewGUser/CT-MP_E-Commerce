from flask import Blueprint, request, jsonify
from models import Order, OrderItem, Product
from connect_to_db import db
from marshmallow import ValidationError

orders_bp = Blueprint('orders_bp', __name__)

# 1. Place an Order
@orders_bp.route('/orders', methods=['POST'])
def place_order():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        customer_id = data.get('customer_id')
        items = data.get('items')  # Expecting a list of product_id and quantity

        if not customer_id or not items:
            return jsonify({'error': 'Missing customer_id or items'}), 400

        total_price = 0
        order_items = []

        # Create Order Items and calculate total price
        for item in items:
            if 'product_id' not in item or 'quantity' not in item:
                return jsonify({'error': 'Each item must have a product_id and quantity'}), 400

            product = Product.query.get_or_404(item['product_id'])
            quantity = item['quantity']

            if quantity <= 0:
                return jsonify({'error': f'Quantity for product {product.id} must be greater than zero'}), 400

            total_price += product.price * quantity

            order_item = OrderItem(
                product_id=product.id,
                quantity=quantity,
                product_price=product.price
            )
            order_items.append(order_item)

        # Create Order
        new_order = Order(
            customer_id=customer_id,
            total_price=total_price,
            order_items=order_items
        )

        db.session.add(new_order)
        db.session.commit()

        return jsonify({'message': 'Order placed successfully'}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of failure
        return jsonify({'error': str(e)}), 500

# 2. Retrieve an Order by ID
@orders_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    try:
        order = Order.query.get_or_404(id)
        order_items = [{'product_id': item.product_id, 'quantity': item.quantity, 'product_price': item.product_price} for item in order.order_items]

        return jsonify({
            'order_id': order.id,
            'customer_id': order.customer_id,
            'order_date': order.order_date,
            'total_price': order.total_price,
            'items': order_items
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. Retrieve all Orders (Order History)
@orders_bp.route('/orders', methods=['GET'])
def get_all_orders():
    try:
        orders = Order.query.all()
        all_orders = []

        for order in orders:
            order_items = [{'product_id': item.product_id, 'quantity': item.quantity, 'product_price': item.product_price} for item in order.order_items]
            all_orders.append({
                'order_id': order.id,
                'customer_id': order.customer_id,
                'order_date': order.order_date,
                'total_price': order.total_price,
                'items': order_items
            })

        return jsonify(all_orders), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
