import math

yaricap = float (input("Çemberin yarıçap uzunluğunu giriniz: "))
aci = float(input("Daire diliminin açısını giriniz: "))

alan= (aci / 360) * math.pi * yaricap * yaricap
alan = round(alan, 4)

print(f"Yarıçapı {yaricap} ve açısı {aci} derece olan dairenin alanı = {alan}")