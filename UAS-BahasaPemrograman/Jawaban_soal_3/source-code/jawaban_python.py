import tkinter as tk

def on_button_click():
    label.config(text="Halo, Selamat Datang!")

# Buat jendela utama
root = tk.Tk()
root.title("Contoh GUI")

# Buat label
label = tk.Label(root, text="Tekan tombol di bawah")
label.pack(pady=10)

# Buat tombol
button = tk.Button(root, text="Klik Saya", command=on_button_click)
button.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
