def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Tidak bisa membagi dengan nol."
    except TypeError:
        return "Error: Tipe data tidak valid. Pastikan kedua argumen adalah angka."
    else:
        return f"Hasil pembagian: {result}"


print(divide_numbers(10, 2))   # Hasil yang valid
print(divide_numbers(10, 0))   # Pembagian dengan nol
print(divide_numbers(10, "a")) # Tipe data tidak valid