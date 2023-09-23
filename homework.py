import sqlite3

with sqlite3.connect('users.db') as db:
    cr = db.cursor()
    cr.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT
                )''')
    
    cr.execute('''INSERT INTO users (name, email) VALUES
    ('mark', 'user1@gmail.com'),
    ('Daniel', 'user2@outlook.com'),
    ('Irina', 'user3@gmail.com')
                ''')
    
    cr.execute('''SELECT name FROM users WHERE email LIKE '%@gmail.com'
            
               ''')
    
    result = cr.fetchall()
    for res in result:
        print(f"{res[0]}")