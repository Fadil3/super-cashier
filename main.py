from update import update
from input import inputNama, inputInteger

data_item = []

print(r"""\
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
print(r"""\
+-------------+--------+
|   Menu      | Hotkey |
+-------------+--------+
| Input item  |      1 |
| Update item |      2 |
| Delete item |      3 |
| List item   |      4 |
| Keluar      |      0 |
+-------------+--------+
""")
print("Masukkan pilihan menu sesuai hotkey")

while True:
    menu = input("Pilihan menu: ")
    if menu == "1":
        print("Menu Belanja")
        while True:
            nama = inputNama()
            jumlah = inputInteger("jumlah")
            harga = inputInteger("harga")
            total = int(jumlah) * int(harga)
            item = {
                'nama': nama,
                'jumlah': jumlah,
                'harga': harga,
                'total': total
            }
            data_item.append(item)
            print("Lanjutkan input ? (y/n)")
            continue_input = input()
            if continue_input == "n" or continue_input == "N":
                break
    elif menu == "2":
        print("Update item")
        # print all item
        for item in data_item:
            print("Nama: " + item['nama'])
            print("Jumlah: " + str(item['jumlah']))
            print("Harga: " + str(item['harga']))
            print("Total: " + str(item['total']))
            print("")

        print("Pilih item yang akan diupdate: ")
        nama_item = input()

        print("Pilih field yang akan diupdate: ")
        print("1. Nama")
        print("2. Jumlah")
        print("3. Harga")
        # print("4. Total")
        print("0. Batal")
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
        # print all item
        for item in data_item:
            print("Nama: " + item['nama'])
            print("Jumlah: " + item['jumlah'])
            print("Harga: " + item['harga'])
            print("Total: " + str(item['total']))
            print("")
        print("1. Hapus item tertentu \n2. Hapus semua item")
        pilihan = input()
        if pilihan == "1":
            print("Pilih item yang akan dihapus: ")
            nama_item = input()
            for item in data_item:
                if item['nama'] == nama_item:
                    data_item.remove(item)
                    print("Item berhasil dihapus")
                    break
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
        for item in data_item:
            print("Nama: " + item['nama'])
            print("Jumlah: " + str(item['jumlah']))
            print("Harga: " + str(item['harga']))
            print("Total: " + str(item['total']))
            print("")
    elif menu == "0":
        print("Keluar")
        break
    else:
        print("Menu tidak tersedia")
