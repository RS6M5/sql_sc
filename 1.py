import sqlite3

# Подключение к базе данных (если базы данных не существует, она будет создана)
conn = sqlite3.connect('school_data.db')
cursor = conn.cursor()

# Создание таблицы students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных и таблица 'students' успешно созданы.")