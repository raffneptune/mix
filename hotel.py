import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class HotelSejukAsri:
    def __init__(self, root):
        self.root = root
        self.root.title("Raffi - Hotel Sejuk Asri")

        # Frame utama
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack()

        # Bingkai input
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding=(20, 10))
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        tk.Label(input_frame, text="Hotel Sejuk Asri").grid(row=0, column=0, columnspan=2, pady=5)
        tk.Label(input_frame, text="=====================================").grid(row=1, column=0, columnspan=2, pady=5)

        # Nama Petugas
        tk.Label(input_frame, text="Input Nama Petugas :").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.nama_petugas = tk.Entry(input_frame)
        self.nama_petugas.grid(row=2, column=1, padx=10, pady=5)

        # Nama Customer
        tk.Label(input_frame, text="Input Nama Customer :").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.nama_customer = tk.Entry(input_frame)
        self.nama_customer.grid(row=3, column=1, padx=10, pady=5)

        # Tanggal Check-In
        tk.Label(input_frame, text="Input Tanggal Check-In :").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.tanggal_checkin = tk.Entry(input_frame)
        self.tanggal_checkin.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="=====================================").grid(row=5, column=0, columnspan=2, pady=5)

        # Kode Kamar
        tk.Label(input_frame, text="Pilih Kode Kamar[M/S/L/A]:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.kode_kamar = tk.Entry(input_frame)
        self.kode_kamar.grid(row=6, column=1, padx=10, pady=5)

        # Lama Sewa
        tk.Label(input_frame, text="Input Lama Sewa (Hari) :").grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.lama_sewa = tk.Entry(input_frame)
        self.lama_sewa.grid(row=7, column=1, padx=10, pady=5)

        # Tombol Proses
        tk.Button(input_frame, text="Proses", command=self.proses_transaksi).grid(row=8, column=0, columnspan=2, pady=10)

        # Bingkai output
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding=(20, 10))
        output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.result = tk.Text(output_frame, width=55, height=20, state='disabled')
        self.result.pack()

        # Frame untuk input uang bayar dan proses pembayaran
        self.pembayaran_frame = tk.Frame(main_frame, padx=10, pady=10)
        self.pembayaran_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.pembayaran_frame.grid_remove()

        tk.Label(self.pembayaran_frame, text="Input Uang Bayar :").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.uang_bayar = tk.Entry(self.pembayaran_frame)
        self.uang_bayar.grid(row=0, column=1, padx=10, pady=5)

        # Tombol Pembayaran
        tk.Button(self.pembayaran_frame, text="Bayar", command=self.proses_pembayaran).grid(row=1, column=0, columnspan=2, pady=10)

    def proses_transaksi(self):
        try:
            # Ambil input dari user
            self.nama_petugas_val = self.nama_petugas.get()
            self.nama_customer_val = self.nama_customer.get()
            self.tanggal_checkin_val = self.tanggal_checkin.get()
            self.kode_kamar_val = self.kode_kamar.get().upper()
            self.lama_sewa_val = int(self.lama_sewa.get())

            # Tentukan nama kamar dan harga sewa
            if self.kode_kamar_val == 'M':
                self.nama_kamar_val = "Melati"
                self.harga_sewa_val = 650000
            elif self.kode_kamar_val == 'S':
                self.nama_kamar_val = "Sakura"
                self.harga_sewa_val = 550000
            elif self.kode_kamar_val == 'L':
                self.nama_kamar_val = "Lily"
                self.harga_sewa_val = 400000
            elif self.kode_kamar_val == 'A':
                self.nama_kamar_val = "Anggrek"
                self.harga_sewa_val = 350000
            else:
                messagebox.showerror("Error", "Kode kamar tidak valid!")
                return

            # Hitung jumlah bayar
            self.jumlah_bayar_val = self.harga_sewa_val * self.lama_sewa_val

            # Hitung PPN (diskon)
            if self.lama_sewa_val > 5:
                self.diskon_val = 0.10
            elif self.lama_sewa_val > 3:
                self.diskon_val = 0.05
            else:
                self.diskon_val = 0.0

            self.ppn_val = self.diskon_val * self.jumlah_bayar_val
            self.total_bayar_val = self.jumlah_bayar_val - self.ppn_val

            # Tampilkan hasil
            self.result.config(state='normal')
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, f"             Bukti Pemesanan Kamar\n")
            self.result.insert(tk.END, f" \t\tHotel Sejuk Asri\n")
            self.result.insert(tk.END, f" =====================================================\n")
            self.result.insert(tk.END, f" Nama Petugas : {self.nama_petugas_val}\t\t\t  Nama Customer : {self.nama_customer_val}\n")
            self.result.insert(tk.END, f" \t\t\t  Tanggal Check-in : {self.tanggal_checkin_val}\n")
            self.result.insert(tk.END, f" =====================================================\n")
            self.result.insert(tk.END, f" Nama Kamar Yang Di Pesan : {self.nama_kamar_val}\n")
            self.result.insert(tk.END, f" Harga Sewa Per malam : Rp. {self.harga_sewa_val}\n")
            self.result.insert(tk.END, f" Lama Sewa : {self.lama_sewa_val} hari\n")
            self.result.insert(tk.END, f" PPN 10% : Rp. {self.ppn_val}\n")
            self.result.insert(tk.END, f" Jumlah Bayar : Rp. {self.jumlah_bayar_val}\n")
            self.result.insert(tk.END, f" Total Bayar : Rp. {self.total_bayar_val}\n")
            self.result.config(state='disabled')

            # Tampilkan frame pembayaran
            self.pembayaran_frame.grid()

        except ValueError:
            messagebox.showerror("Error", "Input tidak valid!")

    def proses_pembayaran(self):
        try:
            uang_bayar = float(self.uang_bayar.get())
            uang_kembali = uang_bayar - self.total_bayar_val

            # Tampilkan hasil pembayaran
            self.result.config(state='normal')
            self.result.insert(tk.END, f" Uang Bayar: Rp. {uang_bayar}\n")
            self.result.insert(tk.END, f" Uang Kembali: Rp. {uang_kembali}\n")
            self.result.config(state='disabled')

        except ValueError:
            messagebox.showerror("Error", "Input tidak valid!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelSejukAsri(root)
    root.mainloop()