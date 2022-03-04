daftar_buku =  ['Seven Habits', 'How To Influence People', 'First Things First']
print("\nTampilkan Daftar Buku")
print(daftar_buku)

print("\nTampilkan semua buku")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan salah satu buku misal buku ke-3")
print(daftar_buku[2])

print("\nTampilkan buku ke 2&3 dengan for range")
for i in range (1,len(daftar_buku)):
    print(daftar_buku[i])

print("\nTampilkan type data yang berbeda elemennya")
daftar_buku = (1, "Kenji volume 2", -313, 3.4)
print(daftar_buku)

print("\nKembalikan ke daftar awal")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First']
print("\nTambahkan 1 buku")
daftar_buku.append("Dunia Matematika")
for buku in(daftar_buku):
    print(buku)

print("\nTampilkan dengan for range")
for i in range (2,len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear list")
daftar_buku.clear()
for i in range (1,len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti elemen pertama")
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Things First']
daftar_buku[0] = 'Eight Habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nAmbil elemen kedua")
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nTampilkan elemen yang diambil")
print(buku)

print("\nSisa buku")
daftar_buku.pop()
for i in range (0,len(daftar_buku)):
    print(daftar_buku[i])