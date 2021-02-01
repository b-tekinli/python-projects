import random

dnaSample = ["A","T","C","G"]
dnaCollection = []
eslesmeOranlari = []

for i in range(1,200,1):
    satir = []
    for t in range(0,300,1):
        satir.append(random.sample(dnaSample,1))
    dnaCollection.append(satir)

for t in range(1,199,1):
    eslesme = 0
    for a in range(0,300,1):
        if dnaCollection[0][a] == dnaCollection[t][a]:
            eslesme = eslesme + 1
    eslesmeOran = eslesme / 3
    eslesmeOran = round(eslesmeOran, 3)
    print(t, ". kişi hasta ile {eslesmeOran} uyuşma sağladı.")
    eslesmeOranlari.append(eslesmeOran)

enBuyuk = eslesmeOranlari[0]
kisiSiraNo = 1
for i in range(1, 199, 1):
    if eslesmeOranlari[i - 1] > enBuyuk:
        enBuyuk = eslesmeOranlari[i - 1]
        kisiSiraNo = i + 1
print(kisiSiraNo, enBuyuk)
