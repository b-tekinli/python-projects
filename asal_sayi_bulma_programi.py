print("\nASAL SAYILARI BULMA PROGRAMI\n")

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
                else:
                    print(sayi)

sayi1 = int(input("Sayı 1: "))
sayi2 = int(input("Sayı 2: "))

asalSayilariBul(sayi1, sayi2)