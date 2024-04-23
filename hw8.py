import sqlite3

# CRUD - create reed update delete
db = sqlite3.connect('op8-hw')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    hobby TEXT,
    first_name TEXT,
    last_name TEXT,
    birth_year INTEGER,
    homework_score INTEGER
)''')

print('Все студенты')
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

db.commit()

cursor.execute('''SELECT * FROM students WHERE LENGTH(last_name) > 10''')
print("\nСтуденты, чьи фамилии длиннее 10 символов:")
for row in cursor.fetchall():
    print(*row, sep='  ')


cursor.execute('''UPDATE students SET first_name = 'genius' WHERE homework_score > 10''')
#
cursor.execute("SELECT * FROM students WHERE first_name = 'genius'")
print("\n'genius' студенты:")
for row in cursor.fetchall():
    print(*row, sep='  ')

db.commit()
db.close()
#



