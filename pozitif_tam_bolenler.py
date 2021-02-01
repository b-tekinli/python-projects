sayi = int(input("Pozitif tam sayı: "))

print(f"{sayi} sayısının tam bölenleri:")
print("1", end="")

for i in range(2, sayi + 1):
    if(sayi % i == 0):
        print(",{i}", end ="")