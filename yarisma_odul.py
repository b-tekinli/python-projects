cevapList = []
odulList = []

verilecekOdulSayisi = int(input("Lütfen verilecek ödül sayısını giriniz: "))
dogruCevap = input("Doğru cevabı giriniz: ")
cevapVerenKisiSayisi = int(input("Cevap veren kişi sayısı: "))

for i in range(1, cevapVerenKisiSayisi + 1, 1):
    if dogruCevap == input(f"{i}. cevap veren kişinin cevabını giriniz: "):
        odulList.append(i)
i = 0
if int(len(odulList)) < (verilecekOdulSayisi - 1):
    while i <= int(len(odulList)) - 1:
        print(odulList[i])
        i = i + 1
else:
    while i <= verilecekOdulSayisi - 1:
        print(odulList[i])
        i = i + 1
print("numaralı kişiler ödül almaya hak kazanmıştır.")