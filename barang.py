class Barang:
    def __init__(self, nama, kode, jumlah):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah

def tambah_barang(inventaris):
    nama = input("\nMasukkan nama barang: ")
    kode = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    barang_baru = Barang(nama, kode, jumlah)
    inventaris.append(barang_baru)
    print("Barang berhasil ditambahkan!")

def tampilkan_semua_barang(inventaris):
    if not inventaris:
        print("\nInventaris kosong.")
    else:
        print("\nDaftar Barang:")
        for barang in inventaris:
            print("Nama:", barang.nama)
            print("Kode:", barang.kode)
            print("Jumlah:", barang.jumlah)
            print("--------------------")

def cari_barang(inventaris, kode):
    for barang in inventaris:
        if barang.kode == kode:
            print("Barang ditemukan:")
            print("Nama:", barang.nama)
            print("Kode:", barang.kode)
            print("Jumlah:", barang.jumlah)
            return barang
    print("Barang dengan kode", kode, "tidak ditemukan.")
    return None

def hapus_barang(inventaris, kode):
    for barang in inventaris:
        if barang.kode == kode:
            inventaris.remove(barang)
            print("Barang dengan kode", kode, "telah dihapus.")
            return
    print("Barang dengan kode", kode, "tidak ditemukan.")

def main():
    inventaris_barang = []
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Semua Barang")
        print("3. Cari Barang berdasarkan Kode")
        print("4. Hapus Barang berdasarkan Kode")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_barang(inventaris_barang)

        elif pilihan == '2':
            tampilkan_semua_barang(inventaris_barang)

        elif pilihan == '3':
            kode = input("\nMasukkan kode barang yang ingin dicari: ")
            cari_barang(inventaris_barang, kode)

        elif pilihan == '4':
            kode = input("\nMasukkan kode barang yang ingin dihapus: ")
            hapus_barang(inventaris_barang, kode)

        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan program ini.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()