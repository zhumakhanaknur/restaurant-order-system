from database import get_db

def process_payment(order_id):
    db = get_db()
    order = db.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()

    if not order:
        db.close()
        return {"success": False, "message": "Тапсырыс табылмады."}

    # Demo project: real bank/payment API is intentionally simulated.
    db.execute(
        "UPDATE orders SET payment_status = 'paid', status = 'new' WHERE id = ?",
        (order_id,),
    )
    db.commit()
    db.close()

    return {"success": True, "message": "Төлем сәтті өтті."}
