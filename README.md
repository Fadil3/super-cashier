     $$$$$$\                                                  
    $$  __$$\                                                 
    $$ /  \__$$\   $$\ $$$$$$\  $$$$$$\  $$$$$$\              
    \$$$$$$\ $$ |  $$ $$  __$$\$$  __$$\$$  __$$\             
     \____$$\$$ |  $$ $$ /  $$ $$$$$$$$ $$ |  \__|            
    $$\   $$ $$ |  $$ $$ |  $$ $$   ____$$ |                  
    \$$$$$$  \$$$$$$  $$$$$$$  \$$$$$$$\$$ |                  
     \______/ \______/$$  ____/ \_______\__|                  
                      $$ |                                    
     $$$$$$\          $$ |     $$\      $$\                   
    $$  __$$\         \__|     $$ |     \__|                  
    $$ /  \__|$$$$$$\  $$$$$$$\$$$$$$$\ $$\ $$$$$$\  $$$$$$\  
    $$ |      \____$$\$$  _____$$  __$$\$$ $$  __$$\$$  __$$\ 
    $$ |      $$$$$$$ \$$$$$$\ $$ |  $$ $$ $$$$$$$$ $$ |  \__|
    $$ |  $$\$$  __$$ |\____$$\$$ |  $$ $$ $$   ____$$ |      
    \$$$$$$  \$$$$$$$ $$$$$$$  $$ |  $$ $$ \$$$$$$$\$$ |      
     \______/ \_______\_______/\__|  \__\__|\_______\__|

# super-cashier
Super cashier adalah aplikasi kasir dalam bentuk terminal. Dibuat dengan `python` dan `sqlite`.

## Background project
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya dengan harapan 
Customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
Customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

## Fitur yang tersedia
    +-------------+--------+
    |   Menu      | Hotkey |
    +-------------+--------+
    | Input item  |      1 |
    | Update item |      2 |
    | Delete item |      3 |
    | List item   |      4 |
    | Check Order |      5 |
    | Checkout    |      6 |
    | Keluar      |      0 |
    +-------------+--------+
1. `Input item` berfungsi untuk memasukan barang yang ingin dibeli oleh `customer`. Attribut yang diinput adalah `nama barang`, `jumlah barang`, dan `harga barang`.
Berikut ini kode untuk input.
```python
nama = input_nama()
jumlah = input_integer("jumlah")
harga = input_integer("harga")
total = int(jumlah) * int(harga)
diskon = discount(total)
harga_diskon = total - diskon
item = {
 'nama': nama,
 'jumlah': jumlah,
 'harga': harga,
 'total': total,
 'diskon': diskon,
 'harga_diskon': harga_diskon
 }
data_item.append(item)
```

Setiap input, akan ada diskon yang dihitung dengan potongan 5%, 6%, dan 7%.
```python
def discount(total):
    disc = 0
    if total >= 200_000:
        disc = (total * 0.05)
        print("Selamat anda mendapatkan diskon 5%")
    elif total >= 300_000:
        disc = (total * 0.06)
        print("Selamat anda mendapatkan diskon 6%")
    elif total >= 500_000:
        disc = (total * 0.07)
        print("Selamat anda mendapatkan diskon 7%")
    return disc
```

2. `Update item` berfungsi untuk update barang yang dibeli oleh `customer`. Customer bisa memilih nama, jumlah, atau harga untuk diupdate.
Berikut ini kode untuk `update`.
```python
def update (data , nama , field , value ) : 
  for item in data : 
    if item [ 'nama' ]   ==   nama : 
      item [ field ]   =   value     
  return   data
```

3. `Delete item` berfungsi untuk menghapus barang yang dibeli oleh `customer`. Barang dapat dihapus secara satuan atau langsung semua barang.
Berikut ini kode untuk `delete`.
```python
data_item.pop(int(index_item) - 1)
```

4. `List item` berfungsi untuk menampilkan barang yang dibeli oleh `customer`.
Berikut ini kode untuk `List item`.
```python
def print_data_item():
    if len(data_item) == 0:
        print("Belum ada item yang dimasukkan")
        return
    for item in data_item:
        print(f"Nama: {item['nama']}")
        print(f"Jumlah: {item['jumlah']:,}")
        print(f"Harga: {item['harga']:,}")
        print(f"Total: {item['total']:,}")
        print(f"Diskon: {item['diskon']:,}")
        print(f"Harga Diskon: {item['harga_diskon']:,}\n")
```
5. `Check Order` berfungsi untuk memeriksa apakah barang yang diinput oleh `customer` sudah sesuai format atau belum.
Berikut ini kode untuk `Check Order`.
```python
def check_order(order):
    # check theres no empty fields in the order
    for item in order:
        if len(item['nama']) == 0 or item['jumlah'] == 0 or item['harga'] == 0 or item['total'] == 0 or (item['diskon']) < 0 or item['harga_diskon'] < 0:
            print("===\nMasukkan nama barang !!!\n===")
            return
    return print("Pemesanan sudah benar\n")
```

6. `Checkout` berfungsi untuk memasukkan barang yang diinput oleh `customer` ke database.
Berikut ini kode untuk `Checkout`.
```python
import sqlite3

def check_out(data):
    con = sqlite3.connect('cashier.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS transactions (no_id INTEGER PRIMARY KEY AUTOINCREMENT, nama_item TEXT,jumlah_item INTEGER, harga INTEGER,  total_harga INTEGER, diskon INTEGER, harga_diskon INTEGER)')

    cur.executemany('INSERT INTO transactions (nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon) VALUES (:nama, :jumlah, :harga, :total, :diskon, :harga_diskon)', data)

    con.commit()
    con.close()
```

7. `Keluar` berfungsi untuk keluar dari loop program.

## Cara Menggunakan Program
1. Clone / download repository ini.
2. Buka terminal ditempat file program didownload.
3. Jalankan `python main.py`.

## Hasil Test Case

1. Menambahkan dua item baru

![image](https://user-images.githubusercontent.com/55126764/232300681-a8092813-8f1f-4ec6-b552-06c187d3536b.png)

2. Delete item

![image](https://user-images.githubusercontent.com/55126764/232300887-f2b4c708-b97d-4d9a-911a-2bf5a7ad40fc.png)

3. Hapus semua item

![image](https://user-images.githubusercontent.com/55126764/232301201-ba3c56af-f6a0-48c9-a325-c60036a1cbfc.png)

4. Checkout

![image](https://user-images.githubusercontent.com/55126764/232301528-645cdea6-0cb4-4482-8f45-c15099b431bf.png)

Berhasil masuk ke database
![image](https://user-images.githubusercontent.com/55126764/232301719-609bc074-1318-481a-aa27-a6f37873895b.png)



