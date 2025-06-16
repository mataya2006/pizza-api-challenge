from . import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    # Relationship: one restaurant has many RestaurantPizzas
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

