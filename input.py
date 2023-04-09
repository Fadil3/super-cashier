def input_nama():
    nama = input("Masukkan nama barang: ")
    if len(nama) == 0:
        print("===\nMasukkan nama barang !!!\n===")
        return input_nama()
    return nama


def input_integer(nama):
    try:
        angka = int(input(f"Masukkan {nama} barang: "))
        if angka < 0:
            print("===\nMasukkan angka positif\n===")
            return input_integer(nama)
        return angka
    except ValueError:
        print("Masukkan angka !!!")
        return input_integer(nama)
