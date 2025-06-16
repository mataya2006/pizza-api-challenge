from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Restaurant, Pizza, db

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []

    # Validate price
    if not isinstance(price, int) or not (1 <= price <= 30):
        errors.append("Price must be between 1 and 30")

    # Validate foreign keys exist
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        errors.append("Pizza not found")

    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        errors.append("Restaurant not found")

    if errors:
        return jsonify({"errors": errors}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(rp)
    db.session.commit()

    response = {
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }

    return jsonify(response), 201
