daftar_buku = ['Seven habits','How to influence people','First thing first','4dx']
print("\ntampilkan semua daftar buku")
print(daftar_buku)

print("\ntampilkan semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\ntampilkan isi daftar_buku dengan index tertentu")
print(daftar_buku[0])

print("\ntampilkan dengan in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, "kenji volume 2", -313, 3.14, "accounting"]
print("\ntampilkan dengan in range denga tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nkembalikan nilai awal daftar buku")
daftar_buku = ['Seven habits','How to influence people','First thing first','4dx']
print("\ntambahkan 1 buku")
daftar_buku.append('Dunia matematika dunia kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti element pertama")
daftar_buku =  ['Seven habits','How to influence people','First thing first','4dx']
daftar_buku[0]= 'Eight Habit'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nBuku yang diambil tadi")
print(buku)

print("\nSisa buku")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku )
