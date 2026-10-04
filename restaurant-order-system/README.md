# Restaurant Order System

QR арқылы мейрамханада тапсырыс беруге арналған оқу жобасы.

## Технологиялар

- Python
- Flask
- SQLite
- HTML / CSS / JavaScript

## Sequence диаграммаға сәйкестігі

1. Клиент QR кодты сканерлейді → веб интерфейс.
2. Веб интерфейс мәзірді сұрайды.
3. Тапсырыс контроллері мәзірді алады.
4. Дерекқор мәзірді қайтарады.
5. Клиент тағам таңдайды.
6. Төлем расталады.
7. Тапсырыс дерекқорға сақталады.
8. Order ID қайтарылады.
9. Асхана экраны тапсырысты көреді.
10. Тапсырыс статусы жаңартылады.
11. Клиентке тапсырыс қабылданғаны көрсетіледі.

## Іске қосу

### 1. Репозиторийді жүктеу

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd restaurant-order-system
```

### 2. Виртуалды орта

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Flask орнату

```bash
pip install -r requirements.txt
```

### 4. Серверді іске қосу

```bash
python app.py
```

Браузерден:

```text
http://127.0.0.1:5000
```

Асхана экраны:

```text
http://127.0.0.1:5000/kitchen
```

## Ескерту

Бұл оқу жобасында төлем жүйесі демонстрация ретінде жасалған. Нақты банк төлемін қабылдау үшін Kaspi Pay, Freedom Pay, CloudPayments немесе басқа төлем провайдерінің API-ін бөлек қосу керек.
