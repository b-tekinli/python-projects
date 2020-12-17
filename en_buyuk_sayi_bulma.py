sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))

if (sayi1 > sayi2) and (sayi1 > sayi3):
    enBuyuk = sayi1
    print(f"En büyük sayı: {enBuyuk}")
elif (sayi2 > sayi1) and (sayi2 > sayi3):
    enBuyuk = sayi2
    print(f"En büyük sayı: {enBuyuk}")
elif (sayi1 == sayi2) and (sayi3 == sayi2):
    print("Sayılar birbirine eşittir.")
else:
    enBuyuk = sayi3
    print(f"En büyük sayı: {enBuyuk}")
