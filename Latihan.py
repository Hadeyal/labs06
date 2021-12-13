daftarkontak = {"Nama": "Nomor Telepon"}
kontak = {'Hadeyal':'0857781793926', 'Aslah':'0857123456'}

print("="*30)
print("   Nama   |   Nomor Telepon   ")
print("="*30)
print(" # Hadeyal  |   ",kontak['Hadeyal'])
print(" # Aslah    |   ",kontak['Aslah'])
print("="*30)

# Menampilkan Kontak Hadeyal
print("Menampilkan Kontak Hadeyal")
print("="*30)
print(" # Hadeyal  |  ",kontak['Hadeyal'])
print("="*30)

# Menambahkan Kontak dengan Nama Aldi dan Nomor 08561234567
print("Menambah Kontak dengan Nama Aldi dan Nomor Telepon 08561234567")
kontak['Aldi']='08561234567'
print("="*30)
print("  Aldi  |  ",kontak['Aldi'])
print("="*30)
print("  Aldi  |  ",kontak['Aldi'])
print("="*30)

# Mengubah kontak Aslah dengan Nomor Baru 08581234567
print("Mengubah Kontak Aslah dengan Nomor Baru 08581234567")
kontak['Aslah']='08581234567'
print("="*30)
print(" # Aslah  |  ",kontak['Aslah'])
print("="*30)

# Menampilkan Semua Nama
print("Menampilkan Semua Nama")
print("="*30)
print(kontak.keys())
print("="*30)

# Menampilkan Semua Nomor
print("Menampilkan Semua Nomor")
print("="*30)
print(kontak.values())
print("="*30)

# Menampilkan Semua Daftar Kontk Beserta Nama dan Nomornya
print("Menampilkan Daftar Nama dan Nomor")
print("="*30)
print(kontak.items())
print("="*30)

# Menghapus Kontak Aslah
print("Hapus Kontak Aslah")
kontak.pop('Aslah')
print("="*30)
print(kontak.items())
print("="*30)
        
        
    
