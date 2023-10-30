import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
# cursor.execute('CREATE TABLE students (ID INTEGER, first_name TEXT, last_name TEXT, age INTEGER);')
# cursor.execute("INSERT INTO students VALUES (1, 'Jo', 'Black', 25)")
id_number = 2
first_name = 'Sergey'
last_name = 'Gontarenko'
age = 27
insert_query = "INSERT INTO students VALUES (?, ?, ?, ?);"
indira = (3, 'Indira', 'Gontarenko', 26)
family = [
    (1, 'Indira', 'Gontarenko', 26),
    (2, 'Sergey', 'Gontarenko', 27),
    (3, 'Mama Mira', 'Marat', 18),
    (4, 'Mama Ira', 'Gontarenko', 18)
]
# cursor.execute(insert_query, indira)
# for family in family:
#     cursor.execute(insert_query, family)
# cursor.executemany(insert_query, family)
cursor.execute("SELECT * FROM students;")
print(cursor.fetchall())
conn.commit()
conn.close()

