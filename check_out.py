
import sqlite3


def check_out(data):
    con = sqlite3.connect('cashier.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS transactions (no_id INTEGER PRIMARY KEY AUTOINCREMENT, nama_item TEXT,jumlah_item INTEGER, harga INTEGER,  total_harga INTEGER, diskon INTEGER, harga_diskon INTEGER)')

    cur.executemany('INSERT INTO transactions (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES (:nama, :jumlah, :harga, :total, :diskon, :harga_diskon)', data)

    con.commit()
    con.close()
