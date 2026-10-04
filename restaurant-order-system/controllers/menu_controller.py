from database import get_db

def get_menu():
    db = get_db()
    rows = db.execute("SELECT * FROM menu ORDER BY id").fetchall()
    db.close()
    return [dict(row) for row in rows]
