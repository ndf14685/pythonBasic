import sqlite3 

conn = sqlite3.connect("database.sqlite")

cursor = conn.cursor()

#cursor.execute("CREATE TABLE personas (TEXT nombre, NUMERIC edad)")

personas= {
    ("Pedro",26)
    ("Juan",34)
    ("Miguel",24)

    }

for nombre,edad in personas :
    cursor.execute("INSERT INTO personas VALUES (?,?)", nombre,edad)

conn.commit()

cursor.execute("SELECT * FROM personas")

personas = cursor.fetchall()

print(personas)

conn.close()