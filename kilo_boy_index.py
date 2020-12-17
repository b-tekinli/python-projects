print("\nKİLO-BOY İNDEXİ\n")

name = input("Ad: ")
kg = float(input("Kilo: "))
hg = float(input("Boy: "))

index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)

if (index >= 0) and (index <= 18.4):
    print(f" {name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
elif (index > 18.4) and (index <= 24.9):
    print(f" {name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
elif (index > 24.9) and (index <= 29.9):
    print(f" {name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
elif (index >= 29.9) and (index <= 34.9):
    print(f" {name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")
else:
    print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz...")