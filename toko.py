import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Membuat tabel barang jika belum ada
c.execute('''CREATE TABLE IF NOT EXISTS barang
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              nama TEXT NOT NULL, 
              harga REAL NOT NULL, 
              stok INTEGER NOT NULL)''')
conn.commit()

# Fungsi untuk menambah data barang
def input_data_barang():
    def submit():
        nama = entry_nama.get()
        harga = float(entry_harga.get())
        stok = int(entry_stok.get())
        
        c.execute("INSERT INTO barang (nama, harga, stok) VALUES (?, ?, ?)", (nama, harga, stok))
        conn.commit()
        messagebox.showinfo("Info", "Data barang berhasil ditambahkan!")
        window_input.destroy()

    window_input = tk.Toplevel()
    window_input.title("Input Data Barang")

    tk.Label(window_input, text="Nama Barang").grid(row=0, column=0)
    tk.Label(window_input, text="Harga").grid(row=1, column=0)
    tk.Label(window_input, text="Stok").grid(row=2, column=0)

    entry_nama = tk.Entry(window_input)
    entry_harga = tk.Entry(window_input)
    entry_stok = tk.Entry(window_input)

    entry_nama.grid(row=0, column=1)
    entry_harga.grid(row=1, column=1)
    entry_stok.grid(row=2, column=1)

    tk.Button(window_input, text="Submit", command=submit).grid(row=3, column=1)

# Fungsi untuk menampilkan data barang
def tampil_data_barang():
    window_tampil = tk.Toplevel()
    window_tampil.title("Data Barang")

    tree = ttk.Treeview(window_tampil, columns=("ID", "Nama", "Harga", "Stok"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nama", text="Nama")
    tree.heading("Harga", text="Harga")
    tree.heading("Stok", text="Stok")
    tree.pack(fill=tk.BOTH, expand=True)

    c.execute("SELECT * FROM barang")
    rows = c.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Fungsi untuk menghapus data barang
def delete_data_barang():
    def submit():
        id_barang = int(entry_id.get())
        c.execute("DELETE FROM barang WHERE id = ?", (id_barang,))
        conn.commit()
        messagebox.showinfo("Info", "Data barang berhasil dihapus!")
        window_delete.destroy()

    window_delete = tk.Toplevel()
    window_delete.title("Delete Data Barang")

    tk.Label(window_delete, text="ID Barang").grid(row=0, column=0)
    entry_id = tk.Entry(window_delete)
    entry_id.grid(row=0, column=1)

    tk.Button(window_delete, text="Submit", command=submit).grid(row=1, column=1)

# Fungsi untuk mencari data barang
def mencari_data_barang():
    def submit():
        nama = entry_nama.get()
        window_cari_result = tk.Toplevel()
        window_cari_result.title("Hasil Pencarian")

        tree = ttk.Treeview(window_cari_result, columns=("ID", "Nama", "Harga", "Stok"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nama", text="Nama")
        tree.heading("Harga", text="Harga")
        tree.heading("Stok", text="Stok")
        tree.pack(fill=tk.BOTH, expand=True)

        c.execute("SELECT * FROM barang WHERE nama LIKE ?", ('%' + nama + '%',))
        rows = c.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)

        window_cari.destroy()

    window_cari = tk.Toplevel()
    window_cari.title("Mencari Data Barang")

    tk.Label(window_cari, text="Nama Barang").grid(row=0, column=0)
    entry_nama = tk.Entry(window_cari)
    entry_nama.grid(row=0, column=1)

    tk.Button(window_cari, text="Submit", command=submit).grid(row=1, column=1)

# Fungsi untuk menghitung jumlah pembelian
def hitung_jumlah_pembelian():
    def submit():
        id_barang = int(entry_id.get())
        jumlah_beli = int(entry_jumlah.get())
        
        c.execute("SELECT stok FROM barang WHERE id = ?", (id_barang,))
        row = c.fetchone()
        
        if row and row[0] >= jumlah_beli:
            c.execute("UPDATE barang SET stok = stok - ? WHERE id = ?", (jumlah_beli, id_barang))
            conn.commit()
            messagebox.showinfo("Info", "Pembelian berhasil! Stok telah diperbarui.")
        else:
            messagebox.showerror("Error", "Stok tidak mencukupi atau barang tidak ditemukan.")
        
        window_beli.destroy()

    window_beli = tk.Toplevel()
    window_beli.title("Hitung Jumlah Pembelian")

    tk.Label(window_beli, text="ID Barang").grid(row=0, column=0)
    tk.Label(window_beli, text="Jumlah Pembelian").grid(row=1, column=0)
    
    entry_id = tk.Entry(window_beli)
    entry_jumlah = tk.Entry(window_beli)

    entry_id.grid(row=0, column=1)
    entry_jumlah.grid(row=1, column=1)

    tk.Button(window_beli, text="Submit", command=submit).grid(row=2, column=1)

# Fungsi untuk mereset tabel barang
def reset_tabel_barang():
    c.execute("DROP TABLE IF EXISTS barang")
    c.execute('''CREATE TABLE barang
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  nama TEXT NOT NULL, 
                  harga REAL NOT NULL, 
                  stok INTEGER NOT NULL)''')
    conn.commit()
    messagebox.showinfo("Info", "Tabel barang telah direset dan ID telah diatur ulang.")

# Membuat antarmuka utama
root = tk.Tk()
root.title("Raffi - Manajemen Barang")

# Menambahkan label "Toko Raffi" di bagian atas
tk.Label(root, text="Toko Raffi", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Label(root, text="Menu:", font=("Helvetica", 10, "bold")).pack(pady=10)

tk.Button(root, text="Input Data Barang", command=input_data_barang).pack(pady=5)
tk.Button(root, text="Tampil Data Barang", command=tampil_data_barang).pack(pady=5)
tk.Button(root, text="Delete Data Barang", command=delete_data_barang).pack(pady=5)
tk.Button(root, text="Mencari Data Barang", command=mencari_data_barang).pack(pady=5)
tk.Button(root, text="Hitung Jumlah Pembelian", command=hitung_jumlah_pembelian).pack(pady=5)
tk.Button(root, text="Reset ID Barang (Akan Mereset Tabel Barang Juga)", command=reset_tabel_barang).pack(pady=5)

root.mainloop()

conn.close()