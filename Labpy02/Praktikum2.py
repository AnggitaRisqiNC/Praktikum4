# Menggunakan Steatment if
print("Nama : Anggita Risqi Nur Clarita")
print("NIM  : 312210450")

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