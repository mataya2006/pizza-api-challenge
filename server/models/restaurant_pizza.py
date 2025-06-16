from . import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Relationships
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    # Validation on price
    @staticmethod
    def validate_price(price):
        return 1 <= price <= 30
