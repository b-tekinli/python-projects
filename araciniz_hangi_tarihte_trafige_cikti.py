import datetime

print("\nARACINIZ HANGİ TARİHTE TRAFİĞE ÇIKTI?\n")

tarih = input("Aracınız hangi tarihte trafiğe çıktı? (02/04/2020): ")
tarih = tarih.split("/")
trafik = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[1]))
simdi = datetime.datetime.now()
fark = simdi - trafik
days = fark.days

if days > 365:
    print("1. Servis aralığı")
elif (days > 365) and (days <= 365*2):
    print("2. Servis aralığı")
elif (days > 365*2) and (days <= 365*3):
    print("3. Servis aralığı")
else:
    print("Hatalı gün")