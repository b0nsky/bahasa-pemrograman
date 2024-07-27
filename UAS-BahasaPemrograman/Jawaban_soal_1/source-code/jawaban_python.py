# Contoh function
def sapa(nama):
    return f"Halo, {nama}!"

# Menggunakan fungsi
print(sapa("Alice"))

# Contoh recursive
def faktorial(n):
    # Kondisi dasar
    if n == 0 or n == 1:
        return 1
    else:
        # Rekursi
        return n * faktorial(n - 1)

# Menggunakan fungsi rekursif
print(faktorial(5))  