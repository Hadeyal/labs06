# labspy06

# latihan 1
# Untuk latihan kali ini merubah dari fungsi ke lambda Ada 4 fungsi yang harus dirubah ke lambda
![Screenshot_5](https://user-images.githubusercontent.com/81457697/145676287-50f59153-11bc-4ed7-8973-61cb91f4d03d.png)

```python
import math


def a(x):
    return x ** 2


def b(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def c(*args):
    return sum(args) / len(args)


def d(s):
    return "".join(set(s))
```

# Dirubah menggunakan Lambda

```python
aa = lambda x: x ** 2
bb = lambda x, y: math.sqrt(x ** 2 + y ** 2)
cc = lambda *args: sum(args) / len(args)
dd = lambda s: "".join(set(s))
```
```python
print("Latihan a")
print("=========")
print("Fungsi\t = ", (a(4)))
print("Lambda\t = ", (aa(4)))
print()
print("Latihan b")
print("=========")
print("Fungsi\t = ", (b(4, 7)))
print("Lambda\t = ", (bb(4, 7)))
print()
print("Latihan c")
print("=========")
print("Fungsi\t = ", (c(10)))
print("Lambda\t = ", (cc(10)))
print()
print("Latihan d")
print("=========")
print("Fungsi\t = ", (d("abcde")))
print("Lambda\t = ", (dd("abcde")))
```

output
![Screenshot_6](https://user-images.githubusercontent.com/81457697/145677869-7106979e-fabd-4f34-b9b0-676bebcdbe5a.png)

# membuat program sederhana data mahasiswa menggunakan fungsi, untuk menambah, menampilkan, menghapus, dan mengubah pada program tersebut 
# Berikut untuk flowchartnya
![flowchart06](https://user-images.githubusercontent.com/81457697/145693871-c2c15852-efed-4f1c-a927-91a715c1c8f1.png)

![flowchart06_01](https://user-images.githubusercontent.com/81457697/145693875-fb662143-5793-4bf4-9fe0-ad5cddd1fc03.png)

![flowchart06_02](https://user-images.githubusercontent.com/81457697/145693883-c18a10dd-c116-4b7f-9ccd-c8cbbb0656c6.png)


# disini untuk menambah, menampilkan, merubah dan menghapus menggunakan fungsi yaitu def. 

data = {}

```python
def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t\t: "))
    tugas = int(input("NIlai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


def tampilkan():
    if data.items():
        print("================================== Daftar Nilai ======================================")
        print("======================================================================================")
        print("|  No  |      NAMA     |      NIM      |   TUGAS  |   UTS   |   UAS   | NILAI AKHIR  |")
        print("======================================================================================")
        i = 0
        for a in data.items():
            i += 1
            print(f"| {i:4} | {a[0]:13s} | {a[1][0]:17} | {a[1][1]:10d} |  {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("===================================== Daftar Nilai ===================================")
        print("======================================================================================")
        print("|  No  |      NAMA     |      NIM      |   TUGAS  |   UTS   |   UAS   | NILAI AKHIR  |")
        print("======================================================================================")
        print("|                                    Tidak Ada Data                                  |")
    print("======================================================================================")


def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("================================")
        print("====BERHASIL MENGHAPUS DATA====")
        print("================================")
    else:
        print("Data {0} tidak ada".format(nama))


def ubah():
    print("===============================")
    print("===Edit Data Nilai Mahasiswa===")
    print("===============================")
    nama = input("Masukan Nama\t\t: ")
    print("===============================")
    if nama in data.keys():
        nim = input("NIM baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("================================")
        print("=====BERHASIL MENGUBAH DATA=====")
        print("================================")
    else:
        print("Data nilai {0} tidak ada ".format(nama))


while True:
    print("")
    print("================================")
    print("======== DATA MAHASISWA ========")
    print("================================")
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
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break

    else:
        print()
        print("==================================")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("==================================")
```        
# Penjelasan :
-data = {}, disini saya akan menggunakan dictionary untuk menampung data mahasiswa

-Untuk menambah data, menampilkan, mengubah dan menghapus data, sama source codenya seperti source code di tugas 5 hanya saja di masukkan ke dalam fungsi dan saya sedikit merubah tampilannya

-Setelah semua di masukan ke dalam fungsi, maka baru buat perulangan dengan while true dan masukkan fungsi - fungsi ke dalamnya seperti berikut
```python
while True:
    print("")
    print("================================")
    print("======== DATA MAHASISWA ========")
    print("================================")
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
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break

    else:
        print()
        print("==================================")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("==================================")
 ```
 # output nya
 -Tanpa data atau belum ada data yang di inputkan
 
 ![Screenshot_8](https://user-images.githubusercontent.com/81457697/145678140-75f71d8a-540e-4160-8dfb-1b4d0b5172b5.png)

-Dengan ada data

![Screenshot_9](https://user-images.githubusercontent.com/81457697/145678195-f8fd200b-4eeb-40c7-90a6-265fd674a1fd.png)

-Menu Tambah

![Screenshot_10](https://user-images.githubusercontent.com/81457697/145678226-a1626368-2a75-4c9d-9572-d126a3e2d268.png)

-Menu Ubah

![Screenshot_11](https://user-images.githubusercontent.com/81457697/145678376-543af77c-8d2f-464a-aab4-db0f9f64807c.png)

-Setelah mengubah data, lalu melihat data yang diubah

![Screenshot_12](https://user-images.githubusercontent.com/81457697/145678400-f5251c72-0031-433e-8490-782210e71a39.png)

-Menu Hapus

![Screenshot_13](https://user-images.githubusercontent.com/81457697/145678428-57d0abdc-f53e-4bf1-bc64-b95cf26bbfe0.png)

-Menu Keluar

![Screenshot_14](https://user-images.githubusercontent.com/81457697/145678452-bee5b1e7-28fa-4355-a44d-9e39cc801d27.png)

