data = {}


def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t\t: "))
    tugas = int(input("Nilai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


def tampilkan():
    if data.items():
        print("=================================Daftar Nilai============================")
        print("=========================================================================")
        print("| No |   Nama   |   NIM   |   TUGAS   |   UTS   |   UAS   | Nilai Akhir |")
        print("=========================================================================")
        i = 0
        for a in data.items():
            i += 1
            print("| {i=4} | {a[0]:13s]} | {a[1][0]:17} | {a[1][1]:10d} | {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("=================================Daftar Nilai============================")
        print("=========================================================================")
        print("| No |   Nama   |   NIM   |   TUGAS   |   UTS   |   UAS   | NILAI AKHIR |")
        print("=========================================================================")
        print("|                            Tidak Ada Data                              ")
        print("=========================================================================")


def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input("Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("=============================")
        print("===Berhasil Menghapus Data===")
        print("=============================")
    else:
        print("Data {0} tidak ada".format(nama))


def ubah():
    print("===============================")
    print("===Edit Data Nilai Mahasiswa===")
    print("===============================")
    nama = input("Masukan Nama\t\t: ")
    print("===============================")
    if nama in data.keys():
        nim = input("NIM Baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("============================")
        print("===Berhasil Mengubah Data===")
        print("============================")
    else:
        print("Data Nilai {0} tidak ada ".format(nama))


while True:
    print("")
    print("==========================")
    print("======Data Mahasiswa======")
    print("==========================")
    x = input("(L)ihat \n(T)ambah \n(U)bah \n(H)apus \n(K)eluar \nPilih menu : ")
    if x.lower() == "l":
        tampilkan()
    elif x.lower() == "t":
        tambah()
    elif x.lower() == "u":
        ubah()
    elif x.lower() == "h":
        hapus()
    elif x.lower() == "k":
        print()
        print("=============================")
        print("=====Keluar Dari Program=====")
        print("=============================")
        break

    else:
        print()
        print("=================================")
        print("===Pilihan Anda Tidak Tersedia===")
        print("===Pilihlah Menu Yang Tersedia===")
        
            

