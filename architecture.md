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

    subgraph DataAccess ["4. Деректерді өңдеу"]
        D["sqlite3 модулі<br>SQL сұраныстары"]
    end

    subgraph Database ["5. SQLite БД"]
        E[("Кестелер:<br>- users<br>- dishes<br>- orders<br>- order_items<br>- payments")]
    end

    %% Бағытталған протоколдар мен байланыстар
    A1 & A2 & A3 -->|HTTPS| B
    B -->|HTTP REST API| C
    C -->|TCP/IP & SQL| D
    D -->|SQLite Protocol| E
    
    E -->|Rows| D
    D -->|Objects| C
    C -->|JSON| B
    B -->|UI Render| A1 & A2 & A3g