import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "database" / "restaurant.db"

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    db = get_db()

    db.executescript("""
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'new',
        payment_status TEXT NOT NULL DEFAULT 'unpaid',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        menu_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY(order_id) REFERENCES orders(id),
        FOREIGN KEY(menu_id) REFERENCES menu(id)
    );
    """)

    count = db.execute("SELECT COUNT(*) AS c FROM menu").fetchone()["c"]
    if count == 0:
        db.executemany(
            "INSERT INTO menu (name, description, price) VALUES (?, ?, ?)",
            [
                ("Бургер", "Сиыр еті, ірімшік, көкөністер", 1800),
                ("Пицца", "Ірімшік және тауық еті", 2500),
                ("Паста", "Кілегейлі соуспен паста", 2200),
                ("Салат", "Жаңа көкөністерден салат", 1200),
                ("Кола", "Салқын сусын", 600),
            ],
        )
    db.commit()
    db.close()
