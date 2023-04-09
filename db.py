import sqlite3

con = sqlite3.connect('cashier.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS transactions (no_id INTEGER PRIMARY KEY AUTOINCREMENT, nama_item TEXT,jumlah_item INTEGER, harga INTEGER,  total_harga INTEGER, diskon INTEGER, harga_diskon INTEGER)')

cur.execute('INSERT INTO transactions (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES ("Beras", 2, 10000, 20000, 0, 20000)')

con.commit()

for row in cur.execute('SELECT * FROM transactions'):
    print(row)

con.close()

# def insert (db, table, data):
#     # insert data into table
#     pass # do something]
    