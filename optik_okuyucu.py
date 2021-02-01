import random

secenekler = ["A", "B", "C", "D", "E"]
cevaplar = []
dogrular = []
ogrenciSayisi = int(input("Sınava giren öğrenci sayısı: "))
soruSayisi = int(input("Kaç soru soruldu: "))
for i in range(0, ogrenciSayisi + 1, 1):
    satir = []
    for t in range(0, soruSayisi, 1):
        satir.append(random.sample(secenekler, 1))
    cevaplar.append(satir)
for i in range(0, ogrenciSayisi, 1):
    satir = []
    trueSayi = 0
    falseSayi = 0
    for t in range(0, soruSayisi, 1):
        if cevaplar[i][t] == cevaplar[ogrenciSayisi][t]:
            satir.append(True)
            trueSayi = trueSayi +1
        else:
            satir.append(False)
            falseSayi = falseSayi + 1
    satir.append(trueSayi)
    satir.append(falseSayi)
    dogrular.append(satir)
for i in range(0, ogrenciSayisi, 1):
    net = (dogrular[i][soruSayisi] - dogrular[i][soruSayisi + 1] - (dogrular[i][soruSayisi + 1] / 4))
    print(f"{i + 1}. öğrenci {dogrular[i][soruSayisi]} adet doğru {dogrular[i][soruSayisi +1 ]} adet yanlış yapmıştır. NET = {net}")
