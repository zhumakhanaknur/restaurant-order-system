```mermaid
sequenceDiagram
    autonumber
    actor Client as КЛИЕНТ
    participant UI as ВЕБ ИНТЕРФЕЙС
    participant Ctrl as ТАПСЫРЫС КОНТРОЛЛЕРІ
    participant DB as ДЕРЕҚҚОР
    participant Kitchen as АСХАНА ЭКРАНЫ

    Client->>UI: 1. QR СКАНЕРЛЕУ
    UI->>Ctrl: 2. МӘЗІРДІ СҰРАУ
    Ctrl->>DB: 3. ТАҒАМДАРДЫ АЛУ
    DB-->>Ctrl: 4. МЕНЮ ДЕРЕГІ
    Ctrl-->>Client: 5. ТАМАҚ ТАҢДАП, ТӨЛЕМ ЖАСАЙДЫ
    Client->>UI: 6. ТӨЛЕМДІ РАСТАУ
    UI->>Ctrl: 6. ТӨЛЕМДІ РАСТАУ
    Ctrl->>DB: 8. ТАПСЫРЫСТЫ САҚТАУ
    DB-->>Ctrl: 9. ORDER ID
    Ctrl->>Kitchen: 10. ЖАҢА ТАПСЫРЫС ЖІБЕРУ
    Ctrl-->>Client: 11. ТАПСЫРЫС ҚАБЫЛДАНДЫ