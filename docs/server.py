import sqlite3

def get_db_connection():
    conn = sqlite3.connect('restaurant.db')
    conn.row_factory = sqlite3.Row
    return conn

connection = get_db_connection()
print("Деректер базасымен байланыс сәтті орнатылды!")
connection.close()