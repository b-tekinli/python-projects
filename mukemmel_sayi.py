print("\nMÜKEMMEL SAYI")

print("\nBir sayının kendi hariç bölenlerinin toplamı kendine eşit olan sayılara denir. Örnek olarak, 6 mükemmel bir sayıdır. (1+2+3=6)\n")

number = int(input("Sayı giriniz: "))

add = 0

for i in range(1, number):
    if number % i == 0:
        add += i

if number == add:
    print(f"{number} sayısı mükemmel sayıdır.")
else:
    print(f"{number} sayısı mükemmel sayı değildir.")