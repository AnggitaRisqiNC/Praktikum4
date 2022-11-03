# Menghitung laba yang didapatkan
print("Nama : Anggita Risqi Nur Clarita")
print("NIM  : 312210450")

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