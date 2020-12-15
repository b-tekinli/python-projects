# BANKAMATİK UYGULAMASI

BeyzaHesap = {
    "ad": "Beyzanur Tekinli",
    "hesapNo": "123456789",
    "bakiye": 5000,
    "ekHesap": 1500
}

SevvalHesap = {
    "ad": "Şevval Tekinli",
    "hesapNo": "987654321",
    "bakiye": 8000,
    "ekHesap": 550
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (E/H): ")

            if ekHesapKullanimi == "E":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")
        else:
            print("Üzgünüz bakiyeniz yetersiz.")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitinde {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(BeyzaHesap, 5000)
bakiyeSorgula(BeyzaHesap)

print("*"*12)

paraCek(BeyzaHesap, 500)
bakiyeSorgula(BeyzaHesap)