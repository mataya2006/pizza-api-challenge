from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.app import create_app

app = create_app()

with app.app_context():
    # Clear existing data
    print("Deleting existing data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create restaurants
    print("Creating restaurants...")
    r1 = Restaurant(name="Mario's Pizza", address="123 Pizza Street")
    r2 = Restaurant(name="Luigi's Slice", address="456 Mushroom Ave")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Crust Blvd")

    db.session.add_all([r1, r2, r3])

    # Create pizzas
    print("Creating pizzas...")
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni Feast", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Mushrooms, Onions, Peppers")

    db.session.add_all([p1, p2, p3])

    db.session.commit()

    # Create restaurant_pizzas (join table)
    print("Creating restaurant_pizzas...")
    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r2.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=10, restaurant_id=r3.id, pizza_id=p3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Database seeded successfully!")
