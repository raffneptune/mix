class Transaksi:
    def __init__(self, deskripsi, jumlah, jenis):
        self.deskripsi = deskripsi
        self.jumlah = jumlah
        self.jenis = jenis  # "Pemasukan" atau "Pengeluaran"

def tambah_transaksi(data_keuangan):
    deskripsi = input("\nMasukkan deskripsi transaksi: ")
    jumlah = float(input("Masukkan jumlah transaksi: "))
    jenis = input("Masukkan jenis transaksi (Pemasukan/Pengeluaran): ").capitalize()
    if jenis not in ["Pemasukan", "Pengeluaran"]:
        print("Jenis transaksi tidak valid.")
        return
    transaksi_baru = Transaksi(deskripsi, jumlah, jenis)
    data_keuangan.append(transaksi_baru)
    print("Transaksi berhasil ditambahkan!")

def tampilkan_semua_transaksi(data_keuangan):
    if not data_keuangan:
        print("\nBelum ada transaksi.")
    else:
        print("\nDaftar Transaksi:")
        for transaksi in data_keuangan:
            print("Deskripsi:", transaksi.deskripsi)
            print("Jumlah:", transaksi.jumlah)
            print("Jenis:", transaksi.jenis)
            print("--------------------")

def hitung_total_pemasukan(data_keuangan):
    total_pemasukan = sum(transaksi.jumlah for transaksi in data_keuangan if transaksi.jenis == "Pemasukan")
    print("Total Pemasukan:", total_pemasukan)

def hitung_total_pengeluaran(data_keuangan):
    total_pengeluaran = sum(transaksi.jumlah for transaksi in data_keuangan if transaksi.jenis == "Pengeluaran")
    print("Total Pengeluaran:", total_pengeluaran)

def hitung_saldo_akhir(data_keuangan):
    total_pemasukan = sum(transaksi.jumlah for transaksi in data_keuangan if transaksi.jenis == "Pemasukan")
    total_pengeluaran = sum(transaksi.jumlah for transaksi in data_keuangan if transaksi.jenis == "Pengeluaran")
    saldo_akhir = total_pemasukan - total_pengeluaran
    print("Saldo Akhir:", saldo_akhir)

def main():
    data_keuangan = []
    while True:
        print("\nMenu:")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Semua Transaksi")
        print("3. Hitung Total Pemasukan")
        print("4. Hitung Total Pengeluaran")
        print("5. Hitung Saldo Akhir")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            tambah_transaksi(data_keuangan)

        elif pilihan == '2':
            tampilkan_semua_transaksi(data_keuangan)

        elif pilihan == '3':
            hitung_total_pemasukan(data_keuangan)

        elif pilihan == '4':
            hitung_total_pengeluaran(data_keuangan)

        elif pilihan == '5':
            hitung_saldo_akhir(data_keuangan)

        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan program ini.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()