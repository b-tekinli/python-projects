# DİKDÖRTGEN ALAN HESAPLAMASI V1

def dortgen_alan_hesapla_v1():
    kisa_kenar = int(input("Kısa kenar uzunluğunu giriniz: "))
    uzun_kenar = int(input("Uzun kenar uzunluğunu giriniz: "))
    return kisa_kenar * uzun_kenar

print(dortgen_alan_hesapla_v1())


# DAİRE ALAN HESAPLAMASI V1

def daire_alan_hesapla_v1():
    pi = 3.14
    r = float(input("Yarı çapı giriniz: "))
    return pi * (r ** 2)

print(daire_alan_hesapla_v1())


# DİKDÖRTGEN ALAN HESAPLAMASI V2

def dortgen_alan_hesapla_v2():
    kisa_kenar_v2 = int(input("Kısa kenar uzunluğunu giriniz: "))
    uzun_kenar_v2 = int(input("Uzun kenar uzunluğunu giriniz: "))
    return (kisa_kenar_v2 ** 2) * (uzun_kenar_v2 ** 2)
print(dortgen_alan_hesapla_v2())


# DAİRE ALAN HESAPLAMASI V2

def daire_alan_hesapla_v2():
    pi = 3.14
    r2 = float(input("Yarı çapı giriniz: "))
    return (pi * (r2 ** 2)) ** 2
print(daire_alan_hesapla_v2())
