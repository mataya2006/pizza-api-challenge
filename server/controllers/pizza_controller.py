from flask import Blueprint, jsonify
from server.models import Pizza

bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    data = []
    for p in pizzas:
        data.append({
            'id': p.id,
            'name': p.name,
            'ingredients': p.ingredients
        })
    return jsonify(data), 200
