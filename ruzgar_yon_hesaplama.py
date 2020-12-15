print("\nDENİZDEKİ RÜZGAR DURUMUNU VE YÖN GÖSTEREN PROGRAM\n")                      # ekrana mesaj yazdırdık.

info = "1 km/saat = 0,54 knot baz alınarak hesaplanmaktadır."               # bilgi vermek için info değişkenine atadık.
speed = int(input(f"-{info}-\nRüzgar hızını km/saat cinsinden giriniz: "))  # kullanıcıdan bilgi istedik.
knot = 0.54                                                         # rüzgar hızını hesaplamak için sabit değeri atadık.
x = knot * speed                                                            # x değişkeninde rüzgar hızını hesapladık.

if x == 0:                                                                          # koşullarımızı belirttik.
    print(f"{int(x)}: Sakin. -Deniz dümdüz.")
elif x == 1 or x < 4:
    print(f"{int(x)}: Esinti. -Çok küçük dalgacıklar.")    # istenen koşul karşısında ekrana yazdıralacak mesajı girdik.
elif x == 4 or x < 7:
    print(f"{int(x)}: Hafif rüzgar. -Küçük belirgin dalgacıklar.")
elif x == 7 or x < 11:
    print(f"{int(x)}: Tatlı rüzgar. -Dalgacık tepeleri kırmaya başlar.")
elif x == 11 or x < 17:
    print(f"{int(x)}: Orta rüzgar. -Küçük dalgalar büyür.")
elif x == 17 or x < 22:
    print(f"{int(x)}: Sert rüzgar. -Tepeleri beyaz, köpüren 3 metreyi aşan dalgalar, oluşur.")
elif x == 22 or x < 28:
    print(f"{int(x)}: Kuvvetli rüzgar. -Büyük dalgalar oluşur.")
elif x == 28 or x < 34:
    print(f"{int(x)}: Hafif fırtına. -Deniz kabarmaya başlar.")
elif x == 34 or x < 41:
    print(f"{int(x)}: Fırtına. -7m civarında yüksek dalgalar oluşur.")
elif x == 41 or x < 48:
    print(f"{int(x)}: Kuvvetli fırtına. -Yüksek dalga tepeleri yuvarlanmaya başlar.")
elif x == 48 or x < 56:
    print(f"{int(x)}: Tam fırtına. -12 metreye kadar yüksek dalgalar gözlenir, deniz genellikle beyaz görünür.")
elif x == 56 or x < 64:
    print(f"{int(x)}: Çok şiddetli fırtına. -/11-15m dalga boyu/")
elif 64 >= x:
    print(f"{int(x)}: Kasırga.-Gökyüzü köpükle kaplanır,görüş mesafesi çok düşer 14m'den büyük dalgalar görülmektedir.")
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz...")

direction = int(input("0-360 derece arasında yön bilgisi giriniz: "))               # kullanıcıdan bilgi istedik.

if (338 == direction or 338 < direction <= 360) or (0 == direction or direction <= 22):
    print(f"{direction}: Yıldız / Kuzey")
elif 23 == direction or direction <= 67:                                            # yön için koşullar belirttik.
    print(f"{direction}: Poyraz / Kuzey")
elif 68 == direction or direction <= 112:
    print(f"{direction}: Gündoğusu / Doğu")          # belirtilen koşul sağlandığında ekrana yazdıralacak mesajı girdik.
elif 113 == direction or direction <= 157:
    print(f"{direction}: Keşişleme / Güneydoğu")
elif 158 == direction or direction <= 202:
    print(f"{direction}: Kıble / Güney")
elif 203 == direction or direction <= 247:
    print(f"{direction}: Lodos / Güneybatı")
elif 248 == direction or direction <= 292:
    print(f"{direction}: Güneybatısı / Batı")
elif 293 == direction or direction <= 337:
    print(f"{direction}: Karayel / Kuzeybatı")
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz...")                      # ekrana hata mesajı verdik.
