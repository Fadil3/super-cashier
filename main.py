from update import update
from input import input_nama, input_integer
from discount import discount
from check_order import check_order
from check_out import check_out

data_item = []


def print_menu():
    print(r"""
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
""")


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


print(r"""
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
""")
print("Menu yang tersedia: ")
print_menu()
print("Masukkan pilihan menu sesuai hotkey")

while True:
    menu = input("Pilihan menu: ")
    if menu == "1":
        print("Menu Belanja")
        while True:
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
                'harga_diskon': harga_diskon}
            data_item.append(item)
            print("Lanjutkan input ? (y/n)")
            continue_input = input()
            if continue_input == "n" or continue_input == "N":
                print_menu()
                break
    elif menu == "2":
        print("Update item")
        # print all item
        print_data_item()

        print("Pilih item yang akan diupdate: ")
        nama_item = input()

        print("Pilih field yang akan diupdate: ")
        print("1. Nama\n2. Jumlah\n3. Harga\n0. Batal")

        field = input()
        if field == "1":
            print("Masukkan nama baru: ")
            value = input()
            data_item = update(data_item, nama_item, 'nama', value)
        elif field == "2":
            print("Masukkan jumlah baru: ")
            value = input()
            data_item = update(data_item, nama_item, 'jumlah', value)
        elif field == "3":
            print("Masukkan harga baru: ")
            value = input()
            data_item = update(data_item, nama_item, 'harga', value)
        elif field == "0":
            print("Batal")
            break
        else:
            print("Field tidak tersedia")
    elif menu == "3":
        print("Delete item")
        print("1. Hapus item tertentu \n2. Hapus semua item")
        pilihan = input()
        if pilihan == "1":
            print_data_item()
            print("Pilih item yang akan dihapus (masukkan angka urutan):  ")
            index_item = input()
            try:
                data_item.pop(int(index_item) - 1)
                print("Item berhasil dihapus")
            except IndexError:
                print("Item tidak ditemukan")
                continue
        elif pilihan == "2":
            print("Apakah anda yakin ingin menghapus semua item? (y/n)")
            pilihan = input()
            if pilihan == "y" or pilihan == "Y":
                data_item = []
                print("Semua item berhasil dihapus")
            else:
                print("Batal menghapus semua item")
    elif menu == "4":
        print("List item")
        # print all item
        print_data_item()
    elif menu == "5":
        print("Check Order")
        check_order(data_item)
    elif menu == "6":
        print("Checkout")
        # total harga
        total_harga = 0
        print_data_item()
        for item in data_item:
            total_harga += item['harga_diskon']
        print(f"Total harga: {total_harga:,}")
        check_out(data_item)
    elif menu == "0":
        print("Keluar")
        break
    else:
        print("Menu tidak tersedia")
