# Pizza Restaurant API

A simple Flask API for managing pizza restaurants and their menus.

## Setup

1. Clone repo and install dependencies:
```bash
git clone https://github.com/yourname/pizza-api.git
cd pizza-api
pip install -r requirements.txt
```

2. Set up database:
```bash
export FLASK_APP=app.py
flask db init
flask db migrate
flask db upgrade
```

3. Run the app:
```bash
flask run
```

## API Endpoints

### Restaurants
- `GET /restaurants` - List all restaurants
- `GET /restaurants/<id>` - Get restaurant details
- `DELETE /restaurants/<id>` - Delete a restaurant

### Pizzas
- `GET /pizzas` - List all pizzas

### Restaurant Pizzas
- `POST /restaurant_pizzas` - Add pizza to restaurant menu

## Example Requests

Get all restaurants:
```bash
curl http://localhost:5000/restaurants
```

Add pizza to restaurant:
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"price":10,"pizza_id":1,"restaurant_id":1}' \
http://localhost:5000/restaurant_pizzas
```