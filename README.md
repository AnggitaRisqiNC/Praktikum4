# Praktikum 4
_Anggita Risqi Nur Clarita (312210450) TI.22.A.4_

### Daftar Isi <br>
| No | Description | Link |
|----|----|----|
|1| Flowchart Labpy02 |[Click Here](#flowchart-menentukan-bilangan-terbesar-dari-3-buah-bilangan)|
|2| Algoritma Labpy02 |[Click Here](#algoritma-menentukan-bilangan-terbesar-dari-3-buah-bilangan)|
|3| Program (rumus) Labpy02 |[Click Here](#program-menentukan-bilangan-terbesar-dari-3-buah-bilangan)|
|4| Flowchart Latihan 1 |[Click Here](#flowchart-latihan-1)|
|5| Algoritma Latihan 1 |[Click Here](#algoritma-latihan-1)|
|6| Program (rumus) Latihan 1 |[Click Here](#program-untuk-latihan-1)|
|7| Flowchart Latihan 2 |[Click Here](#flowchart-latihan-2)|
|8| Algoritma Latihan 2 |[Click Here](#algoritma-latihan-2)|
|9| Program (rumus) Latihan 2 |[Click Here](#program-untuk-latihan-2)|
|10| Agoritma Program 1 |[Click Here](#algoritma-program-1)|
|11| Program (rumus) Program 1 |[Click Here](#program-untuk-program-1-praktikum-3)|

# Labpy02 (Praktikum 2)
## Membuat Program Menentukan Bilangan Terbesar dari 3 Buah Bilangan
### Flowchart Menentukan Bilangan Terbesar dari 3 Buah Bilangan
Pertama buat flowchart terlebih dahulu
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Flowchart%20Praktikum2.png)
---

### Algoritma Menentukan Bilangan Terbesar dari 3 Buah Bilangan
1. Mulai
2. Masukkan nilai a, b, c.
3. Lalu gunakan perintah _int(input(" = "))_, tergantung sesuai versi python, jika versi 2 pakai _input(" ")_.
4. Menentukan bilangan terbesar dari a, b, c dengan menggunakan _statement if_.
5. Jika a lebih besar dari b dan c maka cetak nilai a, jika b lebih besar dari a dan c maka cetak nilai b, jika tidak keduanya maka cetak nilai c.
6. Selesai

### Program Menentukan Bilangan Terbesar dari 3 Buah Bilangan
ketikkan rumusnya seperti dibawah ini.
```python
    def pengulangan():
        print("Program Menentukan Bilangan Terbesar dari 3 Bilangan")
        a = int(input ("Masukan Nilai ke-1 = "))
        b = int(input ("Masukan Nilai ke-2 = "))
        c = int(input ("Masukan Nilai ke-3 = "))

        if a>b and a>c:
            print("Nilai Terbesar :", a)
        elif b>a and b>c:
            print("Nilai Terbesar :", b)
        else :
            print("Nilai Terbesar :", c)

        print('')
        print('ingin coba lagi? (ya/tidak)')
        x = input()
        if x == 'ya':
            return pengulangan()
        if x == 'tidak':
            print('Selesai.')

    pengulangan()
```

![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Praktikum2.png)
---
maka setelah itu Run rumusnya
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Praktikum2%20(Run).png)
---
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Praktikum2%20(Run)1.png)
---

# Labspy03 (Praktikum 3)
## Latihan 1 (Perulangan)
### Flowchart Latihan 1
Buatlah flowchart terlebih dahulu.
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Flowchart%20Latihan1.png)
---

### Algoritma latihan 1
Menampilkan N bilangan acak yang lebih kecil dari *0,5*, nilai N diisi pada saat _runtime_.
1. Mulai
2. Memasukan/ import fungsi RANDOM terlebih dahulu.
3. Deklarasi integer, masukkan jumlah N :
4. Memasukan deskripsi kombinasi for untuk menyelesaikannya.
5. Mencetak data ke 1 sampai N dengan hasil nilai kurang dari *0,5*.
6. Selesai

### Program untuk Latihan 1
Ketikkan rumusnya seperti dibawah ini.
```python
    print("Menampilkan bilangan acak yang lebih kecil dari 0.5")
    import random

    jumlah = int(input("Masukkan Nilai N : "))
    a = 0

    for i in range(jumlah):
        a +=1
        b = random.uniform(.0,.5)
        print("data ke:",a,"==>",b)

    print("Selesai")
```

![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Latihan1.png)
---
Kemudian Run rumusnya
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Latihan1%20(Run).png)
---

## Latihan 2 (Perulangan)
### Flowchart Latihan 2
Buatlah Flowchart terlebih dahulu.
1[image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Flowchart%20Latihan2.png)
---

### Algoritma Latihan 2
1. Mulai
2. int max = 0 _Fungsi dari max untuk mencari nilai tertinggi._
3. Menggunakan fungsi perulangan *while true*, hingga menampilkan perulangan sampai batas tertentu. _While disebut uncounted loop (perulangan yang tak terhitung), untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya._
4. Memasukan bilangan integer pada "a".
5. Menggunakan fungsi *if* jika max kurang dari nilai a, maka max sama dengan a.
6. Mengunakan fungsi *if* jika nilai a adalah 0 maka fungsi break artinya perulangan berhenti jika menulis nilai 0.
7. Mencetak nilai paling terbesar setelah *break*, sehingga menampilkan nilai terbesar diantara bilangan tersebut dalam perulangan.
8. Selesai

### Program untuk Latihan 2
Ketikkan Rumusnya seperti dibawah ini.
```python
max = 0 # Menentukan bilangan terbesar
    while True :
        a = int(input("Masukkan bilangan = "))
        if max < a:
            max = a
        if a== 0:
        break # Mengakhiri perulangan

    print ("Bilangan terbesar adalah: ",max)
```

![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Latihan2.png)
---
Kemudian Run rumus tersebut.
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Latihan2%20(Run).png)
---

## Program 1 (Praktikum 3)
_Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba, pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya._

### Algoritma Program 1
Penyelesaian menggunakan For, if

1. Mula-mula masukkan modal usahanya yaitu a = 100000000

2. Gunakan perintah *for m in range (1,9):*, for ini untuk perulangan dari 1 sampai 8, kenapa menggunakan for,karena for ini perulangan yang terhitung. Pada skirp in range(1, 9) akan mebentuk list perulangan yang berisi [1,2,3,4,5,6,7,8] nah dan bahwa iterasi 9 itu tidak termasuk, untuk membuktikan bawa perulangan ini hanya sampai 8 saja.

3. Lalu gunakan *perintah _if(m>=1 and m<=2): b=a*0*. if pertama ini untuk menentukan laba bulan ke 1 dan ke 2.masukan variable kalikan nilai (a) dengan data bulan 1 dan 2. lalu *print("Laba bulan ke-",m," :",b)* untuk menampilkan hasil laba. pada bulan pertama dan kedua belum mendapatkan laba jadinya 0.

4. *if(m>=3 and m<=4): c=a*0.1*. if yang kedua ini untuk menentukkan laba bulan ke 3 dan ke 4.masukan variable kalikan nilai (a) dengan data bulan 3 dan 4. pada bulan ke 3 itu baru mendapatkan laba sebesar 1% berarti bulan ke 4 juga sama. lalu cetak (m) dan (c), dengan perintah *print("Laba bulan ke-",m," :",c)*.

5. Kemudian *if(m>5 and m<=7): d=a*0.5*. if ketiga untuk menentukan laba bulan ke 5 sampai ke 7.masukan variable lalu kalikan nilai (a) dengan data bulan 5 sampai 7, pada bulan ke 5 laba naik sebesar 5% berarti pada bulan ke 6 dan 7 kenaikan labanya sama, lalu cetak (m) dan (d), dengan perintah *print ("Laba bulan ke-",m," :",d)*.

6. *if(m==8): e=a*0.2*. if keempat atau yang terakhir ini untuk menentukan laba bulan ke 8. lalu masukan variabel kalikan nilai (a) dengan data bulan 8. Pada laba bulan ke 8 ini menurun sebanyak 2%, lalu cetak (m) dan (e) dengan perintah *print ("Laba bulan ke-",m," :",e)*.

7. Kemudian yang terakhir totalkan keseluruhan laba yaitu *total = b+b+c+c+d+d+d+e*

8. lalu *print("\nTotal : ", total)*, untuk menampilkan hasil keseluruhan laba dari bulan pertama sampai bulan kedelapan.

9. Selesai

### Program untuk Program 1 (Praktikum 3)
Ketikkan rumusnya seperti dibawah ini.
```python
    a = 100000000
    for m in range(1,9):
        if (m>=1 and m<=2):
            b=a*0
            print("Laba bulan ke-", m, "sebesar:", b)
        if (m>=3 and m<=4):
            c=a*0.1
            print("Laba bulan ke-", m, "sebesar:", c)
        if (m>=5 and m<=7):
            d=a*0.5
            print("Laba bulan ke-", m, "sebesar:", d)
        if (m==8):
            e=a*0.2
            print("Laba bulan ke-", m, "sebesar:", e)
    total = b+b+c+c+d+d+d+e

    print("Total laba adalah : ",total)
```

![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Program1.png)
---
Kemudian Run rumus tersebut.
![image](https://github.com/AnggitaRisqiNC/Praktikum4/blob/main/screenshots/Program1%20(Run).png)
---
# Selesai~
Timakasi