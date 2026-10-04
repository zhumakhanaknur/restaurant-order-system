from database import get_db

def create_order(data):
    items = data.get("items", [])
    if not items:
        return {"success": False, "message": "Тапсырыс бос болмауы керек."}

    db = get_db()
    total = 0
    normalized = []

    for item in items:
        menu_id = int(item["menu_id"])
        quantity = int(item["quantity"])
        if quantity <= 0:
            continue

        menu = db.execute("SELECT * FROM menu WHERE id = ?", (menu_id,)).fetchone()
        if not menu:
            db.close()
            return {"success": False, "message": f"Menu item {menu_id} табылмады."}

        total += menu["price"] * quantity
        normalized.append((menu_id, quantity))

    if not normalized:
        db.close()
        return {"success": False, "message": "Жарамды тағам таңдалмады."}

    cursor = db.execute(
        "INSERT INTO orders (total, status, payment_status) VALUES (?, 'new', 'unpaid')",
        (total,),
    )
    order_id = cursor.lastrowid

    db.executemany(
        "INSERT INTO order_items (order_id, menu_id, quantity) VALUES (?, ?, ?)",
        [(order_id, menu_id, quantity) for menu_id, quantity in normalized],
    )
    db.commit()
    db.close()

    return {"success": True, "order_id": order_id, "total": total}

def get_order(order_id):
    db = get_db()
    order = db.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
    if not order:
        db.close()
        return None

    items = db.execute("""
        SELECT m.name, m.price, oi.quantity
        FROM order_items oi
        JOIN menu m ON m.id = oi.menu_id
        WHERE oi.order_id = ?
    """, (order_id,)).fetchall()

    result = dict(order)
    result["items"] = [dict(row) for row in items]
    db.close()
    return result
