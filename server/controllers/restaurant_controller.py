from flask import Blueprint, jsonify, abort
from server.models import Restaurant, RestaurantPizza, db

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    data = []
    for r in restaurants:
        data.append({
            'id': r.id,
            'name': r.name,
            'address': r.address
        })
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = []
    for rp in r.restaurant_pizzas:
        pizzas.append({
            'id': rp.id,
            'price': rp.price,
            'pizza': {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            }
        })

    return jsonify({
        'id': r.id,
        'name': r.name,
        'address': r.address,
        'pizzas': pizzas
    }), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(r)
    db.session.commit()
    return '', 204
