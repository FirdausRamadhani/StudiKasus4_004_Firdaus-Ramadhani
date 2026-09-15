produk = {
    "motor1" : {
    "nama" : "Vario 125",
    "harga" : "27000000",
    "stok" : "10",
    },

    "motor2" : {
    "nama" : "ZX25r",
    "harga" : "90000000",
    "stok" : "6",
    },

}

while True:
    print("\n====== Dealer Ciel Balap ======")
    print("         ===== Menu =====")
    print("\n1. Lihat Semua Produk")
    print("2. Tambah Kategori Produk")
    print("3. Ubah Harga Produk")
    print("4. Hapus Kategori Produk")
    print("5. Keluar")

    pilihan = input("pilih menu : ")

    if pilihan == "1":
        print("\n===== Semua Produk =====")

        for i in produk:
            print("\nNama Produk : ", produk[i]["nama"])
            print("Harga       : ", produk[i]["harga"])
            print("Stok        : ", produk[i]["stok"])

            if "warna" in produk :
                print("warna   : ", produk[i]["warna"])
                

    elif pilihan == "2" :
        pilih = input("Pilih produk (motor1/motor2) : ")
        warna = input ("Masukkan warna : ")

        produk[pilih]["warna"] = warna

        print(produk)
        print("\nKategori Berhasil Ditambahkan.")


    elif pilihan == "3" :
        nama = input("Masukkan Nama Produk (motor1/motor2): ")

        if nama in produk:
            harga_baru = int(input("Masukkan Harga Baru : "))
            produk[nama]["harga"] = harga_baru
            print("Harga telah diperbarui.")
        else:
            print("Produk Tidak Ditemukan.")

    elif pilihan == "4" :
        pilih_produk = input("Pilih produk yang ingin dihapus (motor1/motor2): " )
        hapus_kategori = input("Masukkan kategori yang ingin dihapus : ")
        del produk[pilih_produk][hapus_kategori]
        print(produk)

    elif pilihan == "5" :
        print("=== Terima Kasih telah menggunakan program ===")
        break
    else :
        print("Pilihan tidak Valid.")