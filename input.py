def inputNama():
    nama = input("Masukkan nama barang: ")
    if len(nama) == 0:
        print("Masukkan nama barang")
        return inputNama()
    return nama


def inputInteger(nama):
    try:
        angka = int(input(f"Masukkan {nama} barang: "))
        if angka < 0:
            print("Masukkan angka positif")
            return inputInteger()
        return angka
    except ValueError:
        print("Masukkan angka !!!")
        return inputInteger()
