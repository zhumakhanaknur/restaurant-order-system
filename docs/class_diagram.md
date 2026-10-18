```mermaid
classDiagram
    class User {
        +int User_id
        +string name
        +string phone
        +string role
        +login()
        +logout()
    }

    class Order {
        +int order_id
        +int table_number
        +double total_amount
        +string status
        +DateTime created_at
        +calculateTotal()
        +updateStatus()
        +sendToKitchen()
    }

    class Dish {
        +int dish_id
        +string name
        +double price
        +string category
        +boolean is_availible
        +update_price()
        +toogleAvailability()
    }

    class OrderItem {
        +int item_id
        +int dish_id
        +int quantity
        +double price
        +getItemSubtotal()
    }

    class Payment {
        +int payment_id
        +int order_id
        +double amount
        +string payment_type
        +processPayment()
        +generateReceit()
    }

    User "1" --> "*" Order
    Dish "1" --> "*" OrderItem
    OrderItem "*" --> "1" Order
    Order "1" --> "1" Payment