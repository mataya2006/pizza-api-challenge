from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant import Restaurant

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    data = [{
        'id': r.id,
        'name': r.name,
        'address': r.address
    } for r in restaurants]
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({ 'error': 'Restaurant not found' }), 404

    data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        } for rp in restaurant.restaurant_pizzas]
    }
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({ 'error': 'Restaurant not found' }), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

