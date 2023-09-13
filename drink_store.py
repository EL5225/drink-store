barang = {"nama": ["Ultramilk", "Grean Tea", "Teh Pucuk"], "harga": [5000, 6000, 3000],
          "stok": [10, 5, 20]}

db = {"nama": [], "harga": [], "jumlah": []}

index_barang = 0
jumlah_barang = 0


def tampil_barang():
    print("=" * 50)
    print("=" * 16, "BARANG TERSEDIA", "=" * 17)
    print("=" * 50)
    for i in range(0, len(barang["nama"]) & len(barang["harga"]) & len(barang["stok"]), 1):
        print(barang["nama"][i], "-- Harga Rp", barang["harga"]
              [i], "-- stok tersedia ", barang["stok"][i])
    print("=" * 50)
    kembali_menu()


def main_menu():

    print("=" * 31)
    print("=" * 5, "TOKO MINUMAN SEGARZ", "=" * 5)
    print("=" * 31)
    print("[1] List Barang tersedia      |")
    print("[2] Edit Barang tersedia      |")
    print("[3] Pembelian                 |")
    print("[4] Daftar Belanja            |")
    print("[5] Pembayaran                |")
    print("[6] Keluar                    |")
    print("=" * 31)

    pilih = input("Pilihan : ")
    print("=" * 31, "\n")

    if pilih == "1":
        tampil_barang()
    elif pilih == "2":
        edit_data()
    elif pilih == "3":
        beli_barang()
    elif pilih == "4":
        daftar_belanja()
    elif pilih == "5":
        bayar()
    elif pilih == "6":
        print("===Keluar===")
    else:
        print("DATA TIDAK ADA")


def kembali_menu():
    print("\n")

    u = input("Kembali ke menu? [y/t] : ")
    if u == "y":
        main_menu()
    elif u == "t":
        print("=" * 16)
        print("=====KELUAR=====")
        print("=" * 16)
        print("...")
        print("..")
        print(".")

    print("\n")


def edit_data():
    print("=" * 50)
    print("=" * 14, "EDIT BARANG TERSEDIA", "=" * 14)
    print("=" * 50)
    print("[1] Edit barang")
    print("[2] Tambah barang")
    pilih2 = input("Pilihan : ")

    if pilih2 == "1":
        print("[1] Edit nama barang")
        print("[2] Edit harga barang")
        print("[3] Edit stok barang")
        pilih3 = input("Pilihan : ")

        if pilih3 == "1":
            for j in range(0, len(barang["nama"]), 1):
                print("[", j, "]", barang["nama"][j])

            nabar = input("Pilih nomor barang : ")
            nabar2 = input("Nama barang baru  : ")
            barang["nama"][int(nabar)] = nabar2

        elif pilih3 == "2":
            for j in range(0, len(barang["nama"]) & len(barang["harga"]), 1):
                print("[", j, "]", barang["nama"][j],
                      "-- Harga Rp", barang["harga"][j])

            habar = input("Pilih nomor barang : ")
            habar2 = input("Harga barang baru  : ")
            barang["harga"][int(habar)] = int(habar2)

        elif pilih3 == "3":
            for j in range(0, len(barang["nama"]) & len(barang["stok"]), 1):
                print("[", j, "]", barang["nama"][j],
                      "-- Stok", barang["stok"][j])

            stobar = input("Pilih nomor barang : ")
            stobar2 = input("Stok barang baru  : ")
            barang["stok"][int(stobar)] = int(stobar2)

    elif pilih2 == "2":
        temp1 = input("Masukan nama barang  : ")
        temp2 = input("Masukan harga barang : ")
        temp3 = input("Masukan stok barang  : ")

        barang["nama"].append(temp1)
        barang["harga"].append(int(temp2))
        barang["stok"].append(int(temp3))

    else:
        print("Data tidak ada")

    kembali_menu()


def beli_barang():
    print("=" * 50)
    print("=" * 16, "PEMBELIAN BARANG", "=" * 16)
    print("=" * 50)
    for j in range(0, len(barang["nama"]) & len(barang["stok"]), 1):
        print("[", j, "]", barang["nama"][j], "-- Stok ", barang["stok"][j])

    index_barang = input("Pilih nomor barang  : ")
    jumlah_barang = input("Jumlah barang  : ")
    jumbar = barang["stok"][int(index_barang)]

    if int(jumlah_barang) > int(jumbar):
        print("Anda membeli lebih dari stok yang tersedia!")
    else:
        jumbar2 = int(jumbar) - int(jumlah_barang)
        barang["stok"][int(index_barang)] = jumbar2

        db["nama"].append(barang["nama"][int(index_barang)])
        db["harga"].append(barang["harga"][int(index_barang)])
        db["jumlah"].append(jumlah_barang)

    kembali_menu()


def daftar_belanja():
    print("=" * 50)
    print("=" * 17, "DAFTAR BELANJA", "=" * 17)
    print("=" * 50)
    if len(db["nama"]) == 0:
        print("Daftar belanja masih kosong. Ayo segera membeli!")
    else:
        for i in range(0, len(db["nama"]) & len(db["harga"]) & len(db["jumlah"]), 1):
            print(db["nama"][i], "-- Harga Rp", db["harga"]
                  [i], "-- Jumlah barang ", db["jumlah"][i])

    kembali_menu()


def bayar():
    print("=" * 51)
    print("=" * 19, "PEMBAYARAN", "=" * 20)
    print("=" * 51)

    if len(db["nama"]) == 0:
        print("Belum ada pembayaran")
        print("Mohon untuk cek kembali daftar belanja")
        kembali_menu()
    else:
        for i in range(0, len(db["nama"]) & len(db["harga"]) & len(db["jumlah"]), 1):
            print(db["nama"][i], "-- Harga Rp", db["harga"]
                  [i], "-- Jumlah barang ", db["jumlah"][i])
        print("="*51)

        total = 0
        for i in range(0, len(db["nama"]) & len(db["harga"]) & len(db["jumlah"]), 1):
            totaltemp1 = db["harga"][i]
            totaltemp2 = db["jumlah"][i]

            total += int(totaltemp1) * int(totaltemp2)

        kembalian = 0
        print("Total Pembayaran : Rp", total, "\n")
        uang = input("Uang pembayaran  : Rp ")
        if int(uang) > int(total):
            kembalian = int(uang) - int(total)
            print("Kembalian        : Rp", kembalian)
            print("=" * 52)
            print("=" * 3, "TERIMA KASIH TELAH BERBELANJA DI TOKO KAMI!", "=" * 4)
            print("=" * 52)

        elif int(uang) == int(total):
            print("Uang pas!")
            print("=" * 52)
            print("=" * 3, "TERIMA KASIH TELAH BERBELANJA DI TOKO KAMI!", "=" * 4)
            print("=" * 52)

        elif int(uang) < int(total):
            print("Uang tidak cukup!")
            kembali_menu()
        else:
            kembali_menu()


main_menu()
