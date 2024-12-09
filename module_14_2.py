import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
 id INTEGER PRIMARY KEY,
 username TEXT NOT NULL,
 email TEXT NOT NULL,
 age INTEGER,
 balance INTEGER NOT NULL
 )
 ''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON users (email)")

# users_data = [
#     ('User1', 'example1@gmail.com', 10, 1000),
#     ('User2', 'example2@gmail.com', 20, 2000),
#     ('User3', 'example3@gmail.com', 30, 3000),
#     ('User4', 'example4@gmail.com', 40, 4000),
#     ('User5', 'example5@gmail.com', 50, 5000),
#     ('User6', 'example6@gmail.com', 60, 6000),
#     ('User7', 'example7@gmail.com', 70, 7000),
#     ('User8', 'example8@gmail.com', 80, 8000),
#     ('User9', 'example9@gmail.com', 90, 9000),
#     ('User10', 'example10@gmail.com', 100, 10000),
# ]
#
# cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)
# for i in range(2, 12, 2):  # идет от 2 до 10, с шагом 2
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

# for i in range(3, 12, 3):  # идет от 3 до 9
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# cursor.execute('SELECT * FROM Users WHERE age != 60')
# rows = cursor.fetchall()
# print("username | email | age | balance")
# print("-----------------------------------------")
# for row in rows:
#     print(f"{row[1]} | {row[2]} | {row[3]} | {row[4]}")
# cursor.execute('DELETE FROM Users WHERE id = ?', (5,))
cursor.execute("SELECT SUM(balance) FROM Users")
total1 = cursor.fetchone()[0]
cursor.execute("SELECT COUNT(*) FROM Users")
total2 = cursor.fetchone()[0]
print(total1)
print(total2)
cursor.execute("SELECT AVG(balance) FROM Users")
avg_age = cursor.fetchone()[0]
print(avg_age)

connection.commit()
connection.close()
