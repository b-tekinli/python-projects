print("HESAP MAKİNESİ")

def topla(sayi1, sayi2):
    return sayi1 + sayi2

def cikar(sayi1, sayi2):
    return sayi1 - sayi2

def carp(sayi1, sayi2):
    return sayi1 * sayi2

def bol(sayi1, sayi2):
    return sayi1 / sayi2

def mod(sayi1, sayi2):
    return sayi1 % sayi2

def us(sayi1, sayi2):
    return sayi1 ** sayi2

islem = input("1.Toplama\n2.Çıkartma\n3.Çarpma\n4.Bölme\n5.Mod Alma\n6.Üs Alma\nYapmak istediğiniz işlemin numarasını giriniz: ")
sayi1 = int(input("İşlem yapmak istediğiniz ilk sayıyı giriniz: "))
sayi2 = int(input("İşlem yapmak istediğiniz ikinci sayıyı giriniz: "))

if islem=="1":
    print(topla(sayi1,sayi2))
elif islem=="2":
    print(cikar(sayi1,sayi2))
elif islem=="3":
    print(carp(sayi1,sayi2))
elif islem=="4":
    print(bol(sayi1,sayi2))
elif islem=="5":
    print(mod(sayi1,sayi2))
elif islem=="6":
    print(us(sayi1,sayi2))
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz..")