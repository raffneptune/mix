class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

def input_mahasiswa():
    nama = input("\nMasukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan program studi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    return Mahasiswa(nama, nim, prodi, nilai)

def tampilkan_data(mahasiswa):
    print("Nama:", mahasiswa.nama)
    print("NIM:", mahasiswa.nim)
    print("Prodi:", mahasiswa.prodi)
    print("Nilai:", mahasiswa.nilai)

def hitung_rata_rata(nilai_mahasiswa):
    total_nilai = sum(nilai_mahasiswa)
    rata_rata = total_nilai / len(nilai_mahasiswa)
    return rata_rata

def main():
    data_mahasiswa = []
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hitung Rata-rata Nilai Mahasiswa")
        print("4. Mahasiswa dengan Nilai Tertinggi")
        print("5. Mahasiswa dengan Nilai Terendah")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            mahasiswa_baru = input_mahasiswa()
            data_mahasiswa.append(mahasiswa_baru)
            print("Data mahasiswa berhasil ditambahkan!")

        elif pilihan == '2':
            if not data_mahasiswa:
                print("\nBelum ada data mahasiswa.")
            else:
                print("\nData Mahasiswa:")
                for mahasiswa in data_mahasiswa:
                    tampilkan_data(mahasiswa)

        elif pilihan == '3':
            if not data_mahasiswa:
                print("\nBelum ada data mahasiswa.")
            else:
                nilai_mahasiswa = [mahasiswa.nilai for mahasiswa in data_mahasiswa]
                rata_rata = hitung_rata_rata(nilai_mahasiswa)
                print("\nRata-rata Nilai Mahasiswa:", rata_rata)

        elif pilihan == '4':
            if not data_mahasiswa:
                print("\nBelum ada data mahasiswa.")
            else:
                mahasiswa_tertinggi = max(data_mahasiswa, key=lambda x: x.nilai)
                print("\nMahasiswa dengan Nilai Tertinggi:")
                tampilkan_data(mahasiswa_tertinggi)

        elif pilihan == '5':
            if not data_mahasiswa:
                print("\nBelum ada data mahasiswa.")
            else:
                mahasiswa_terendah = min(data_mahasiswa, key=lambda x: x.nilai)
                print("\nMahasiswa dengan Nilai Terendah:")
                tampilkan_data(mahasiswa_terendah)

        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan program ini.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()