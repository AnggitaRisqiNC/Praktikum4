# Menentukan Bilangan Terbesar
print("Nama : Anggita Risqi Nur Clarita")
print("NIM  : 312210450")

max = 0 # Menentukan bilangan terbesar
while True :
    a = int(input("Masukkan bilangan = "))
    if max < a:
        max = a
    if a== 0:
       break # Mengakhiri perulangan

print ("Bilangan terbesar adalah: ",max)