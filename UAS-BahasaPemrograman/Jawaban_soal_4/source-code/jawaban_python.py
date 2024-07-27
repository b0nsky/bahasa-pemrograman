import sqlite3

# Membuat koneksi ke database (atau membuat database baru jika belum ada)
conn = sqlite3.connect('contoh.db')

# Membuat cursor untuk berinteraksi dengan database
cursor = conn.cursor()

# Membuat tabel baru
cursor.execute('''
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INTEGER PRIMARY KEY,
    nama TEXT,
    umur INTEGER
)
''')

# Menambahkan data ke tabel
cursor.execute('''
INSERT INTO mahasiswa (nama, umur) VALUES (?, ?)
''', ('Andi', 20))

# Mengambil data dari tabel
cursor.execute('SELECT * FROM mahasiswa')
data_mahasiswa = cursor.fetchall()

# Menampilkan hasil
print("Data Mahasiswa:")
for row in data_mahasiswa:
    print(f'ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}')

# Menyimpan perubahan dan menutup koneksi
conn.commit()
conn.close()