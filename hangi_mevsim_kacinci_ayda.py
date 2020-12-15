season = int(input("Kaçıncı ay?: "))                            # kullanıcıdan kaçıncı ay olduğu bilgisini istedik.

if 12 == season or season <= 2:                                 # season değişkenine 2 koşul belirttik.
    print("Kış")                                                # ekrana kış mevsimi olduğunu yazdırdık.
elif 3 == season or season <= 5:
    print("İlkbahar")                                           # ekrana ilkbahar mevsimi olduğunu yazdırdık.
elif 6 == season or season <= 8:
    print("Yaz")                                                # ekrana yaz mevsimi olduğunu yazdırdık.
elif 9 == season or season <= 11:
    print("Sonbahar")                                           # ekrana sonbahar mevsimi olduğunu yazdırdık.
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz...")  # ekrana hata mesajı verdik.
