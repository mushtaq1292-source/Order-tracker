from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data (order status track karne ke liye)
orders = {
    "09:15": {"buy_orders": 200000, "fulfilled": 120000, "pending": 80000}
}

@app.route('/')
def home():
    return "Order Tracker Web App Running ✅"

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def update_order():
    data = request.json
    time = data.get("time")
    buy_orders = data.get("buy_orders")
    fulfilled = data.get("fulfilled")

    pending = buy_orders - fulfilled
    orders[time] = {"buy_orders": buy_orders, "fulfilled": fulfilled, "pending": pending}
    return jsonify({"msg": "Order updated successfully", "data": orders[time]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
