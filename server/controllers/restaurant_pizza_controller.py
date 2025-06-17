from flask import Blueprint, jsonify, request
from server.models import RestaurantPizza, db
from sqlalchemy.exc import IntegrityError

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify(restaurant_pizza.to_dict()), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Validation error"]}), 400
    
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400