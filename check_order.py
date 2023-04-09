def check_order(order):
    # check theres no empty fields in the order
    for item in order:
        if len(item['nama']) == 0 or item['jumlah'] == 0 or item['harga'] == 0 or item['total'] == 0 or (item['diskon']) < 0 or item['harga_diskon'] < 0:
            print("===\nMasukkan nama barang !!!\n===")
            return
    return print("Pemesanan sudah benar\n")
