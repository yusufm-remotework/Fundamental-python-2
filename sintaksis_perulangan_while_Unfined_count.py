"""
Program perulangan membaca buku dengan while sampai paham
"""
jumlah_buku = 10

print ('Ibu berkata, "Baca Semua buku dan pahami"')

total_jumlah_baca = 0
jumlah_paham =0
print (f"total jumlah baca dan paham {total_jumlah_baca,jumlah_paham}")

while total_jumlah_baca < jumlah_buku:
    total_jumlah_baca = total_jumlah_baca +1
    if jumlah_paham== 5:
        print(f"buku ke {jumlah_paham+1} belum paham")
    else:
        jumlah_paham = jumlah_paham +1
        print(f"buku ke{jumlah_paham} sudah paham")


