-- 1. Барлық тағамдарды бағасы бойынша кему ретімен шығару
SELECT name, price, category, is_available 
FROM dishes 
ORDER BY price DESC;

-- 2. Клиенттер мен олардың тапсырыстарын байланыстырып көру (JOIN)
SELECT u.name AS client_name, o.order_id, o.table_number, o.total_amount, o.status
FROM orders o
JOIN users u ON o.user_id = u.user_id;

-- 3. Категориялар бойынша тағамдардың орташа бағасын есептеу (GROUP BY)
SELECT category, AVG(price) AS average_price, COUNT(*) AS total_dishes
FROM dishes
GROUP BY category;

-- 4. Төлем түрлері бойынша жалпы түскен соманы шығару
SELECT payment_type, SUM(amount) AS total_revenue
FROM payments
GROUP BY payment_type;

-- 5. Белгілі бір шарт бойынша тапсырыстарды сұрыптау (WHERE)
SELECT * FROM orders 
WHERE total_amount > 2000 AND status = 'New';

--8Lab
-- 1. Бірнеше кестені JOIN арқылы біріктіру
SELECT u.name AS client_name, o.order_id, o.table_number, o.status, o.total_amount
FROM orders o
JOIN users u ON o.user_id = u.user_id;
-- 2. Бір жолды ішкі сұраныс: Орташа бағадан қымбат тұратын тағамдарды шығару
SELECT name, price 
FROM dishes 
WHERE price > (SELECT AVG(price) FROM dishes);
-- 3. Бірнеше жолды ішкі сұраныс (IN көмегімен)
SELECT name, price 
FROM dishes 
WHERE category IN (SELECT category FROM dishes WHERE category = 'Негізгі тағам');
-- 4. CASE арқылы шартты мәндер қалыптастыру
SELECT name, price,
    CASE 
        WHEN price > 1500 THEN 'Қымбат'
        ELSE 'Қолжетімді'
    END AS price_category
FROM dishes;
-- 5. Күрделі аналитикалық сұраныс: Әр санат бойынша тағамдардың орташа бағасы және жалпы саны
SELECT category, AVG(price) AS average_price, COUNT(*) AS total_dishes
FROM dishes
GROUP BY category;
