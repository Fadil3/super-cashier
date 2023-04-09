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
