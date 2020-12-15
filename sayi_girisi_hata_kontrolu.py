while True:
    sayi = input("-Çıkmak için 'q' yazınız.-\nSayı:")
    if sayi == "q":
        break

    try:
        result = float(sayi)
        print("Girdiğiniz sayı: ",result)
        break
    except ValueError:
        print("Geçersiz sayı.")
        continue