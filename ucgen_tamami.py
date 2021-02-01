import math
choosed2 = True

def UcgenCevre():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    kenar3 = float (input("Üçüncü kenarın uzunluğunu giriniz: "))

    cevre = kenar1 + kenar2 + kenar3

    return print(f"Kenar uzunlukları {kenar1}, {kenar2}, {kenar3} olan üçgenin çevresi = {cevre}")

def Ucgen2KenarveAci3kenar():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    aci = float (input("İki kenar arasındaki açıyı giriniz: "))

    kenar3 = math.sqrt(kenar1 * kenar1 + kenar2 * kenar2 - 2 * kenar1 * kenar2 * math.cos(math.radians(aci)))
    
    return print(f"1. kenarı {kenar1}, 2. kenarı {kenar2} ve aralarındaki açı {aci} derece olan üçgenin 3. kenarı = {kenar3}")

def UcgenAlan2KenarveDerece():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    aci = float (input("İki kenar arasındaki açıyı giriniz: "))
    
    alan = kenar1 * kenar2 * math.sin(math.radians(aci)) * 1 / 2
    
    return print(f"1. kenar uzunluğu {kenar1}, 2. kenar uzunluğu {kenar2} ve bu kenarlar arasındaki açı {aci} derece olan üçgenin alanı = {alan}")

def UcgenAlan2kenarveDikAci():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    
    alan = (kenar1 * kenar2) / 2
    
    return print(f"1. kenar uzunluğu {kenar1}, 2. kenar uzunluğu {kenar2} ve bu kenarlar arasındaki açı {90} derece olan üçgenin alanı = {alan}")

def UcgenAlanTumKenarlariBilinen():
    kenar1 = float (input("İlk kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("İkinci kenarın uzunluğunu giriniz: "))
    kenar3 = float (input("Üçüncü kenarın uzunluğunu giriniz: "))

    u=(kenar1 + kenar2 + kenar3) / 2
    
    alan=math.sqrt(u * (u - kenar1) * (u - kenar2) * (u - kenar3))
    return print(f"Kenar uzunlukları {kenar1}, {kenar2}, {kenar3} olan üçgenin alanı = {alan}")

def checkChoosed():
    EH= input("Yeni bir hesaplama yapmak ister misiniz(Evet için E'ye, Hayır için H'ye basınız): ")
    if EH == "E":
        main(True)
    elif EH == "H":
        main(False)
    else:
        print("\nSeçiminiz belirlenen aralıkta değil! Lütfen yeniden seçim yapınız...")
        checkChoosed()
    return


def main(choosed2):
    if choosed2 == True:
        choosed = int(input("\n1. Üçgenin çevresini bulmak\n2. 2 kenarı ve açısı bilinen üçgenin 3. kenarını Bulmak\n3. 2 kenarı ve aralarındaki açı bilinen üçgenin alanını bulmak\n4. Dik üçgenin alanını bulmak\n5. Tüm kenarları bilinen üçgenin alanını bulmak\nSeçiminiz: "))

        if choosed == 1:
            UcgenCevre()
        elif choosed == 2:
            Ucgen2KenarveAci3kenar()
        elif choosed == 3:
            UcgenAlan2KenarveDerece()
        elif choosed == 4:
            UcgenAlan2kenarveDikAci()
        elif choosed == 5:
            UcgenAlanTumKenarlariBilinen()
        else:
            print("\nSeçiminiz belirlenen aralıkta değil! Lütfen yeniden seçim yapınız...")
            main(True)
        checkChoosed()
    else:
        print("\nProgramımızı kullandığınız için teşekkür ederiz. İyi Günler :)")
    return

main(choosed2)
