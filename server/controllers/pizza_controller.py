from flask import Blueprint, jsonify
from server.models.pizza import Pizza

bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    data = [{
        'id': p.id,
        'name': p.name,
        'ingredients': p.ingredients
    } for p in pizzas]
    return jsonify(data), 200
