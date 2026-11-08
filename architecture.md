```mermaid
graph TD
    subgraph Client ["1. Клиенттер"]
        A1["Клиент"]
        A2["Даяшы/Аспаз"]
        A3["Әкімші"]
    end

    subgraph Presentation ["2. Frontend"]
        B["HTML, JS, React<br>Себет пен Мәзір"]
    end

    subgraph Business ["3. Backend"]
        C["Python (FastAPI)<br>API мен Логика"]
    end

    subgraph DataAccess ["4. Деректерді өңдеу (SQLite SQL)"]
        D["sqlite3 модулі<br>SQL сұраныстары:<br>- INSERT, UPDATE, DELETE"]
    end

    subgraph Database ["5. SQLite БД"]
        E[("Кестелер:<br>- users<br>- dishes<br>- orders<br>- order_items<br>- payments")]
    end

    A1 & A2 & A3 -->|HTTPS| B
    B -->|REST API| C
    C -->|SQL Queries| D
    D -->|SQL Commands| E
    E -->|Rows / Data| D
    D -->|Python Objects| C
    C -->|JSON| B
    B -->|UI| A1 & A2 & A3