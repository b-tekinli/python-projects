print("\nSAYI TAHMİN OYUNU\n")

import random

sayi=random.randint(1,50)
can = int(input("Kaç hak kullanmak istersiniz?: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puanınız {100 - (100/can) * (sayac-1)}")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")
