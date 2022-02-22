"""
Program perulangan membaca buku dengan while sampai paham
"""
Jumlah_buku = 10

print ('Ibu berkata, "Baca semua bukumu!!"')

total_jumlah_baca =0

Jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}")

while total_jumlah_baca < Jumlah_buku *2:
    total_jumlah_baca = total_jumlah_baca +1
    if Jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"buku ke {Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        Jumlah_buku_yang_sudah_dibaca_dan_dipahami = Jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print (f"Buku ke {Jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")


print(f"Jumlah buku yang sudah dibaca dan dipahami {Jumlah_buku_yang_sudah_dibaca_dan_dipahami}")
