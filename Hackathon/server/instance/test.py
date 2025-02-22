import sqlite3

# Подключаемся к базе данных (или создаем её, если она не существует)
conn = sqlite3.connect(r".\app.db")


# Создаем объект курсора для выполнения SQL-запросов
cursor = conn.cursor()
cursor.execute("SELECT * FROM Review")
rows = cursor.fetchall()

# Выводим все строки
for row in rows:
    print(row)

