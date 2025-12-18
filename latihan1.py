txt = 'Hello World'

# Hitung jumlah karakter
print(len(txt))              # 11

# Ambil karakter terakhir
print(txt[-1])               # d

# Ambil karakter index ke-2 sampai ke-4 ("llo")
print(txt[2:5])              # llo

# Hilangkan spasi
print(txt.replace(" ", ""))  # HelloWorld

# Ubah menjadi huruf besar
print(txt.upper())           # HELLO WORLD

# Ubah menjadi huruf kecil
print(txt.lower())           # hello world

# Ganti karakter H dengan J
print(txt.replace("H", "J")) # Jello World