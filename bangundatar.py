import tkinter as tk
from tkinter import messagebox
import math

def hitung_luas_segi_empat(sisi):
    return sisi * sisi

def hitung_keliling_segi_empat(sisi):
    return 4 * sisi

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def hitung_luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def hitung_keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

class BangunDatarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Raffi - Perhitungan Bangun Datar")
        
        self.menu_label = tk.Label(root, text="Pilih bangun datar untuk menghitung luas dan keliling:")
        self.menu_label.pack()

        self.bangun_datar_var = tk.StringVar()
        self.bangun_datar_var.set("Segi Empat")

        self.bangun_datar_options = ["Segi Empat", "Persegi Panjang", "Segitiga", "Lingkaran"]
        self.bangun_datar_menu = tk.OptionMenu(root, self.bangun_datar_var, *self.bangun_datar_options)
        self.bangun_datar_menu.pack()

        self.show_fields_button = tk.Button(root, text="Tekan untuk memasukkan inputan", command=self.show_input_fields)
        self.show_fields_button.pack()

        self.input_frame = tk.Frame(root)
        self.input_frame.pack()

        self.calculate_button = tk.Button(root, text="Hitung", command=self.calculate_result)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def show_input_fields(self):
        pilihan = self.bangun_datar_var.get()
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.inputs = {}

        if pilihan == "Segi Empat":
            fields = ["Panjang sisi"]
        elif pilihan == "Persegi Panjang":
            fields = ["Panjang", "Lebar"]
        elif pilihan == "Segitiga":
            fields = ["Panjang alas", "Tinggi", "Panjang sisi 1", "Panjang sisi 2", "Panjang sisi 3"]
        elif pilihan == "Lingkaran":
            fields = ["Jari-jari"]

        for field in fields:
            label = tk.Label(self.input_frame, text=field)
            label.pack()
            entry = tk.Entry(self.input_frame)
            entry.pack()
            self.inputs[field] = entry

    def calculate_result(self):
        pilihan = self.bangun_datar_var.get()
        try:
            if pilihan == "Segi Empat":
                sisi = float(self.inputs["Panjang sisi"].get())
                luas = hitung_luas_segi_empat(sisi)
                keliling = hitung_keliling_segi_empat(sisi)
            elif pilihan == "Persegi Panjang":
                panjang = float(self.inputs["Panjang"].get())
                lebar = float(self.inputs["Lebar"].get())
                luas = hitung_luas_persegi_panjang(panjang, lebar)
                keliling = hitung_keliling_persegi_panjang(panjang, lebar)
            elif pilihan == "Segitiga":
                alas = float(self.inputs["Panjang alas"].get())
                tinggi = float(self.inputs["Tinggi"].get())
                sisi1 = float(self.inputs["Panjang sisi 1"].get())
                sisi2 = float(self.inputs["Panjang sisi 2"].get())
                sisi3 = float(self.inputs["Panjang sisi 3"].get())
                luas = hitung_luas_segitiga(alas, tinggi)
                keliling = hitung_keliling_segitiga(sisi1, sisi2, sisi3)
            elif pilihan == "Lingkaran":
                jari_jari = float(self.inputs["Jari-jari"].get())
                luas = hitung_luas_lingkaran(jari_jari)
                keliling = hitung_keliling_lingkaran(jari_jari)
            else:
                raise ValueError("Pilihan tidak valid")
            
            self.result_label.config(text=f"Luas: {luas}\nKeliling: {keliling}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = BangunDatarApp(root)
    root.mainloop()