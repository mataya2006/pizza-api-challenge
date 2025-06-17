from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']
    except KeyError:
        return jsonify({ 'errors': ['Missing required fields'] }), 400

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    if not restaurant_pizza.is_valid():
        return jsonify({ 'errors': ['Price must be between 1 and 30'] }), 400

    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    response = {
        'id': restaurant_pizza.id,
        'price': restaurant_pizza.price,
        'pizza_id': pizza.id,
        'restaurant_id': restaurant.id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }
    return jsonify(response), 201
