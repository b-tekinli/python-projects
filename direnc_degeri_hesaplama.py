print("\n4 BANTLI DİRENÇ DEĞERİ HESAPLAMA\n")                         # ekrana mesaj yazdırdık.

zero = "Siyah"
one = "Kahverengi"
two = "Kırmızı"
three = "Turuncu"                                                     # değişkenlere string değerler atadık.
four = "Sarı"
five = "Yeşil"
six = "Mavi"
seven = "Mor"
eight = "Gri"
nine = "Beyaz"

colors = f"0.{zero} 1.{one} 2.{two} 3.{three} 4.{four}" \
         f"\n5.{five} 6.{six} 7.{seven} 8.{eight} 9.{nine}"              # değişkene değerleri yazdırdık.
print(colors)
first_choose = int(input("İlk basamak için renk seçimi yapınız: "))    # kullanıcıdan bilgi istedik.

print("\n",colors)
second_choose = int(input("İkinci basamak için renk seçimi yapınız: "))# kullanıcı için renkleri tekrar yazdırdık.

multiplier_value = f"\n0.{zero}=0 1.{one}=x10¹ 2.{two}=x10² 3.{three}=x10³ 4.{four}=x10⁴" \
                   f"\n5.{five}=x10⁵ 6.{six}=x10⁶ 7.{seven}=x10⁷ 8.{eight}=x10⁸ 9.{nine}=x10⁹"
print(multiplier_value)
multiplier = int(input("Çarpan değeri için renk seçimi yapınız: "))

if multiplier == 0:                                                    # koşul belirttik.
    resistance = int(str(first_choose) + str(second_choose)*0)         # direnç değerini değişkene atayarak hesaplattık.
    print(f"Direnç değeri: {resistance}")                              # ekrana direnç değerini hesaplayıp yazdırdık.
elif multiplier == 1:
    resistance = int(str(first_choose) + str(second_choose))*10
    print(f"Direnç değeri: {resistance}")
elif multiplier == 2:
    resistance = int(str(first_choose) + str(second_choose))*(10**2)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 3:
    resistance = int(str(first_choose) + str(second_choose))*(10**3)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 4:                                                  # diğer koşulları belirttik.
    resistance = int(str(first_choose) + str(second_choose))*(10**4)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 5:
    resistance = int(str(first_choose) + str(second_choose))*(10**5)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 6:
    resistance = int(str(first_choose) + str(second_choose))*(10**6)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 7:
    resistance = int(str(first_choose) + str(second_choose))*(10**7)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 8:
    resistance = int(str(first_choose) + str(second_choose))*(10**8)
    print(f"Direnç değeri: {resistance}")
elif multiplier == 9:
    resistance = int(str(first_choose) + str(second_choose))*(10**9)
    print(f"Direnç değeri: {resistance}")
else:                                                   # geçersiz ifade girilmesi ihtimali için ekrana mesaj yazdırdık.
    print("Geçersiz değer girdiniz. Lütfen tekrar deneyiniz...")

gold = resistance                                       # altının toleransını hesaplamak için direnç değişkenine atadık.
silver = resistance                                     # gümüşün toleransını hesaplamak için direnç değişkenine atadık.
tolerance = input("\nA) Altın\nB) Gümüş\nTolerans değeri için seçim yapınız: ")
if tolerance == "A":                                    # tolerans için koşul belirttik.
    tolerance_calculate = int((gold*5)/100)             # tolerans hesaplamak için değişkene işlem atadık.
    tolerance_space = (resistance-tolerance_calculate, resistance+tolerance_calculate) # tolerans aralığı hesapladık.
    print(f"\nTolerans: {tolerance_calculate}\nTolerans aralığı: {tolerance_space}")   # tolerans bilgilerini yazdırdık.
elif tolerance == "B":
    tolerance_calculate = int(silver/10)                # tolerans için diğer koşulu belirttik.
    tolerance_space = (resistance-tolerance_calculate, resistance+tolerance_calculate)
    print(f"\nTolerans: {tolerance_calculate}\nTolerans aralığı: {tolerance_space}")   # tolerans bilgilerini yazdırdık.
else:
    print("Geçersiz değer girdiniz. Lütfen tekrar deneyiniz...")                       # ekrana hata mesajı yazdırdık.
