import random

fotograf = []
zipped = []

for i in range(0, 500, 1):
    satir = []
    for t in range(0, 500, 1):
        satir.append(round(random.uniform(0, 255), 0))
    fotograf.append(satir)

for i in range(0, 500, 1):
    for t in range(0, 500, 1):
        satir = []
        if fotograf[i][t] != 0:
            satir.append(i)
            satir.append(t)
            satir.append(fotograf[i][t])
            zipped.append(satir)

print("Orijinal ==> ", 250000)
print("Sıkıştırılmış ==> ", len(zipped))
