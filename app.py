from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import init_db, get_db
from controllers.menu_controller import get_menu
from controllers.order_controller import create_order, get_order
from controllers.payment_controller import process_payment

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/menu")
def menu_page():
    return render_template("menu.html", menu=get_menu())

@app.route("/api/menu")
def menu_api():
    return jsonify(get_menu())

@app.route("/api/orders", methods=["POST"])
def create_order_api():
    data = request.get_json(force=True)
    result = create_order(data)
    return jsonify(result), 201 if result.get("success") else 400

@app.route("/payment/<int:order_id>", methods=["GET", "POST"])
def payment_page(order_id):
    order = get_order(order_id)
    if not order:
        return "Order not found", 404

    if request.method == "POST":
        result = process_payment(order_id)
        if result["success"]:
            return redirect(url_for("order_success", order_id=order_id))
        return render_template("payment.html", order=order, error=result["message"])

    return render_template("payment.html", order=order)

@app.route("/order/<int:order_id>/success")
def order_success(order_id):
    order = get_order(order_id)
    if not order:
        return "Order not found", 404
    return render_template("success.html", order=order)

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

@app.route("/api/kitchen/orders")
def kitchen_orders():
    db = get_db()
    rows = db.execute("""
        SELECT o.id, o.status, o.total, o.created_at,
               GROUP_CONCAT(m.name || ' x' || oi.quantity, ', ') AS items
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.id
        JOIN menu m ON m.id = oi.menu_id
        GROUP BY o.id
        ORDER BY o.created_at DESC
    """).fetchall()
    return jsonify([dict(row) for row in rows])

@app.route("/api/orders/<int:order_id>/status", methods=["POST"])
def update_order_status(order_id):
    data = request.get_json(force=True)
    status = data.get("status")
    allowed = {"new", "preparing", "ready", "completed"}
    if status not in allowed:
        return jsonify({"success": False, "message": "Invalid status"}), 400

    db = get_db()
    db.execute("UPDATE orders SET status = ? WHERE id = ?", (status, order_id))
    db.commit()
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
