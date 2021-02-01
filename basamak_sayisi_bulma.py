print("\nBasamak Sayısı Bulan Program\n")

def basamak(sayi):
    sayac = 1
    while sayi >= 10:
        sayac += 1
        sayi = sayi / 10
    return sayac

sayi = int(input("Lütfen bir sayı girin: "))
print("Girdiğiniz sayının basamak sayısı", basamak(sayi))
