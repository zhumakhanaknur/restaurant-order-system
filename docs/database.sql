-- 1. Қолданушылар кестесі
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
);

-- 2. Тағамдар кестесі (Меню)
CREATE TABLE IF NOT EXISTS dishes (
    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price > 0),
    category TEXT NOT NULL,
    is_available INTEGER DEFAULT 1
);

-- 3. Тапсырыстар кестесі
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    table_number INT NOT NULL,
    total_amount REAL DEFAULT 0.00,
    status TEXT DEFAULT 'Pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- 4. Тапсырыс құрамындағы тағамдар (Байланыс кестесі)
CREATE TABLE IF NOT EXISTS order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT,
    dish_id INT,
    quantity INT NOT NULL CHECK (quantity > 0),
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id)
);

-- 5. Төлемдер кестесі
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT,
    amount REAL NOT NULL,
    payment_type TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Мәліметтер енгізу (INSERT)
INSERT INTO users (name, phone, role) VALUES 
('Ақнур', '+77011234567', 'Client'),
('Арман аспаз', '+77029876543', 'Cook'),
('Дана админ', '+77055554433', 'Admin');

-- Тағамдар кестесін тазалап, жаңадан толтыру
DELETE FROM dishes;

INSERT INTO dishes (dish_id, name, price, category, is_available) VALUES
(1, 'Бургер', 1000, 'Фастфуд', 1),
(2, 'Донер', 1000, 'Фастфуд', 1),
(3, 'Манты', 1000, 'Негізгі тағам', 1),
(4, 'Кока-Кола 0.5', 500, 'Сусын', 1);

INSERT INTO orders (user_id, table_number, total_amount, status) VALUES 
(1, 4, 4800.00, 'New');

INSERT INTO order_items (order_id, dish_id, quantity, price) VALUES 
(1, 1, 1, 2500.00),
(1, 3, 4, 500.00);

INSERT INTO payments (order_id, amount, payment_type) VALUES 
(1, 4800.00, 'Kaspi QR');

-- Мәліметтерді өзгерту (UPDATE)
UPDATE dishes 
SET price = 1800.00 
WHERE name = 'Бургер';

UPDATE orders 
SET status = 'Preparing' 
WHERE order_id = 1;

-- Мәліметтерді жою (DELETE)
-- Ескерту: 3-ші тағамды өшірмес бұрын order_items-те оған сілтеме жоқ екеніне көз жеткізу керек, 
-- әйтпесе foreign key қатесі шығуы мүмкін. Қажет болса бұл жолды аттап өтуге болады.
DELETE FROM dishes 
WHERE dish_id = 3;

