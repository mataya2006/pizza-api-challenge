
# 🍕 Pizza API Challenge

A RESTful API for managing restaurants, pizzas, and their relationships, built with **Flask** and **SQLAlchemy**.

---

## ✅ Setup Instructions

1️⃣ **Clone the Repository**

```bash
git clone <your-repo-url>
cd pizza-api-challenge
```

2️⃣ **Install Dependencies**

```bash
pipenv install
pipenv shell
```

3️⃣ **Database Setup**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4️⃣ **Seed the Database**

```bash
python -m server.seed
```

5️⃣ **Run the Server**

```bash
flask run
```

> The API will run at: `http://127.0.0.1:5000`

---

## 🌐 API Routes Summary

| METHOD | ENDPOINT             | DESCRIPTION                              |
| ------ | -------------------- | ---------------------------------------- |
| GET    | `/restaurants`       | List all restaurants                     |
| GET    | `/restaurants/<id>`  | Get one restaurant (with pizzas)         |
| DELETE | `/restaurants/<id>`  | Delete a restaurant                      |
| GET    | `/pizzas`            | List all pizzas                          |
| POST   | `/restaurant_pizzas` | Add a pizza to a restaurant (with price) |

---

## 📦 Example Requests & Responses

### 🟢 GET `/restaurants`

**Response**

```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  }
]
```

---

### 🟢 GET `/restaurants/1`

**Response**

```json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    }
  ]
}
```

---

### 🔴 DELETE `/restaurants/1`

**Response**

```json
{
  "message": "Restaurant deleted successfully"
}
```

---

### 🟢 GET `/pizzas`

**Response**

```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  }
]
```

---

### 🟢 POST `/restaurant_pizzas`

**Request Body**

```json
{
  "price": 12,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response**

```json
{
  "id": 2,
  "name": "Pepperoni",
  "ingredients": "Tomato, Mozzarella, Pepperoni"
}
```

---

## ✅ Validation Rules

| Field           | Rule                       |
| --------------- | -------------------------- |
| `price`         | Required, Integer (1 - 30) |
| `pizza_id`      | Required, Must exist       |
| `restaurant_id` | Required, Must exist       |

**❗ Error Example:**

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## 📬 Using Postman

1. Import routes manually or ask for **Postman JSON export**.
2. Set base URL: `http://127.0.0.1:5000`
3. Test GET, POST, DELETE requests.
4. For POST requests, set header:

```
Content-Type: application/json
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask SQLAlchemy
* Flask-Migrate
* SQLite

