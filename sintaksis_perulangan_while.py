"""
Program perulangan membaca buku dengan while
"""
Jumlah_buku = 10

print ('Ibu berkata, "Baca semua bukumu!!"')

Jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang dibaca {Jumlah_buku_yang_sudah_dibaca}")

while Jumlah_buku_yang_sudah_dibaca < Jumlah_buku :
    Jumlah_buku_yang_sudah_dibaca = Jumlah_buku_yang_sudah_dibaca +1
    print (f"Buku ke {Jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {Jumlah_buku_yang_sudah_dibaca}")
