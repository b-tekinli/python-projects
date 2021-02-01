# 1 dizi içerisinde elimizdeki kolilerin kiloları bulunmaktadır. Araçlarımız maksimum 300 kilo taşıyabiliyor.
# 300 kiloyu aşan her yük için yeni araç gerekmektedir.
# Verilen diziye göre kaç araca ihtiyaç vardır.

import random

yuk = [5,10,15,20,25,30,35,40,7,14,21,28,35]
yukSayisi = random.randint(0,100)
yukler = []
for i in range(0, yukSayisi, 1):
    yukler.append(random.sample(yuk, 1))
aracSayisi = 1
aracMevcutKilo = 0
i = 0
print("Yük sayısı:", yukSayisi)
print("Yükler:\n", yukler)

while i < (yukSayisi - 1):
    TMP = aracMevcutKilo + int(yukler[i][0])
    if TMP <= 300:
        aracMevcutKilo = TMP
        i = i + 1
    else:
        aracSayisi = aracSayisi + 1
        aracMevcutKilo = 0

if aracMevcutKilo > 0:
    aracMevcutKilo = 0
    aracSayisi = aracSayisi + 1

print(f"Toplam kullanılan araç sayısı= {aracSayisi}")