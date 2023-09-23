import sqlite3

with sqlite3.connect('toys.db') as db:
    cr = db.cursor()
    cr.execute('''CREATE TABLE IF NOT EXISTS toys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT,
                    price REAL,
                    stock_quantity INTEGER
                )''')

    cr.execute(
        """INSERT INTO toys(name, type, price, stock_quantity) VALUES
        ('Пес Патрон', 'plush toy', 9.99, 35),
        ('Мяка ведмедиця', 'plush toy', 10.99, 0), 
        ('Маленький ведмедик', 'plush toy', 9.99, 50),
        ('Великий ведмедик', 'plush toy', 20.99, 50),
        ('Зайчик Star', 'plush toy', 19.99, 30),
        ('SpongeBob', 'plush toy', 29.99, 10),
        ('Patrik', 'plush toy', 12.99, 3),
        ('Лялька Барбі', 'Лялька', 14.99, 60),
        ('Конструктор LEGO Star Wars', 'Конструктор', 49.99, 25),
        ('Набір фарб і пензлів', 'Творчість', 9.99, 40),
        ('Електронна розважальна консоль', 'Електроніка', 99.99, 15),
        ('Гра "Шахи"', 'Настільна гра', 12.99, 35),
        ('Пазли "Пейзаж"', 'Головоломка', 8.99, 75),
        ('Мяч для баскетболу', 'Спортивна іграшка', 19.99, 30),
        ('Робот-трансформер', 'Робот', 29.99, 10)
        """)
    #Виберіть всі м'які іграшки з таблиці "toys", відсортовані за спаданням ціни.
    cr.execute("SELECT name, price FROM toys WHERE type == 'plush toy' ORDER BY price DESC")
    
    result = cr.fetchall()
    for res in result:
        print(f"Назва -- {res[0]}, Ціна -- {res[1]}")
      
    #середня ціна та найменша к-сть на складі м'яких іграшок  
    cr.execute("SELECT ROUND(AVG(price)), MIN(stock_quantity) FROM toys WHERE type == 'plush toy'")                    
    result = cr.fetchall()
    for res in result:
        print(f"середня ціна всіх м'яких іграшок -- {res[0]}",
              f"Найменша к-сть на складі серед м'яких іграшок -- {res[1]}")

    # найвища ціна
    cr.execute('SELECT name, MAX(price) FROM toys ')                  
    result = cr.fetchall()
    for res in result:
        print("Найвища ціна:")
        print(f"Назва -- {res[0]}, Ціна -- {res[1]}")
    #🏓Виберіть імена та ціни всіх м'яких іграшок з таблиці "toys". Додайте стовпець, який визначає категорію ціни так:
    cr.execute("""
                ALTER TABLE toys 
                ADD price_type TEXT;""")
                
    cr.execute("""
                UPDATE toys
                SET price_type =
                    CASE
                        WHEN price <= 10 THEN 'Економний'
                        WHEN price > 10 AND price <= 20 THEN 'Середній'
                        WHEN price > 20 AND price <= 30 THEN 'Високий'
                        ELSE 'Дуже високий'
                    END
               """)
    #🏓Виберіть імена та кількість товару на складі всіх іграшок. Додайте стовпець "discount", де застосуйте знижку відповідно до наступних умов:
    cr.execute("""
               ALTER TABLE toys
               ADD discount INTEGER""")
    cr.execute("""
                UPDATE toys
                SET discount =
                    CASE
                        WHEN stock_quantity >= 50 THEN 10
                        WHEN stock_quantity BETWEEN 20 AND 50 THEN 5
                        ELSE 0
                    END
               """)
    #Перевірка чи все оке
    cr.execute("SELECT * FROM toys")
    result = cr.fetchall()
    for res in result:
        print(f"Назва -- {res[1]}, Ціна -- {res[3]}, К-сть -- {res[4]}, Тип ціни -- {res[5]}, Знижка -- {res[6]}")