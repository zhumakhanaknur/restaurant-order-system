```mermaid
graph TD
    subgraph Client ["1. Клиенттер мен Қызметкерлер"]
        A1["Клиент"]
        A2["Даяшы/Аспаз"]
        A3["Әкімші"]
    end

    subgraph Presentation ["2. Frontend (Интерфейс)"]
        B["HTML, JS, React<br>Себет пен Мәзір"]
    end

    subgraph Business ["3. Backend (Логика)"]
        C["Python (FastAPI)<br>API мен Логика"]
    end

    subgraph DataAccess ["4. Деректерді өңдеу"]
        D["sqlite3 модулі<br>SQL сұраныстары"]
    end

    subgraph Database ["5. SQLite БД"]
        E[("Кестелер:<br>- users<br>- dishes<br>- orders<br>- order_items<br>- payments")]
    end

    %% Сұраныс бағыттары (Кету)
    A1 & A2 & A3 -->|Протокол: HTTPS| B
    B -->|Протокол: HTTP REST API| C
    C -->|Протокол: SQL Queries| D
    D -->|Протокол: SQLite Binary Protocol| E
    
    %% Жауап қайту бағыттары (Қайту - Протоколдар)
    E -->|Протокол: Data Stream / Rows| D
    D -->|Протокол: Python Objects| C
    C -->|Протокол: HTTP Response JSON| B
    B -->|Протокол: HTTPS / DOM Events| A1 & A2 & A3