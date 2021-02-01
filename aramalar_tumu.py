import math
import random

dizi = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
randomsample = random.sample(dizi,1)
aranan = int(randomsample[0])
n = len(dizi)

def LinearSearch(dizi, aranan):
    for i in range(len(dizi)):
        if dizi[i] == aranan:
            return i
    return -1

def JumpSearch(dizi, aranan, n):
    adim = math.sqrt(n)
    onceki = 0
    while dizi[int(min(adim, n)-1)] < aranan:
        onceki = adim
        adim += math.sqrt(n)
        if onceki >= n:
            return -1
    while dizi[int(onceki)] < aranan:
        onceki += 1
        if onceki == min(adim, n):
            return -1
    if dizi[int(onceki)] == aranan:
        return onceki
    return -1

def BinarySearch (dizi, sol, sag, aranan):
    if sag >= sol:
        ortanca = sol + (sag - sol)//2
        ortanca = int(ortanca)
        if dizi[ortanca] == aranan:
            return ortanca
        elif dizi[ortanca] > aranan:
            return BinarySearch(dizi, sol, ortanca - 1, aranan)
        else:
            return BinarySearch(dizi, ortanca + 1, sag, aranan)

    else:
        return -1

def interpolationSearch(dizi, n, aranan):
    dusuk = 0
    yuksek = (n - 1)
    while dusuk <= yuksek and aranan >= dizi[dusuk] and aranan <= dizi[yuksek]:
        pos  = dusuk + int(((float(yuksek - dusuk)/( dizi[yuksek] - dizi[dusuk])) * (aranan - dizi[dusuk])))
        if dizi[pos] == aranan:
            return pos
        if dizi[pos] < aranan:
            dusuk = pos + 1;
        else:
            yuksek = pos - 1;
    return -1

def ExponentialSearch(dizi, n, aranan):
    if dizi[0] == aranan:
        return 0
    i = 1
    while i < n and dizi[i] <= aranan:
        i = i * 2
    return BinarySearch( dizi, i / 2, min(i, n), aranan)

def Chooser():
    print("1.Linear Search (Doğrusal Arama)\n2.Jump Search (Atlamalı Arama)\n3.Binary Search (İkili Arama)\n4.Interpolation Search (Enterpolasyon Arama)\n5.Exponantional Search (Üssel Arama)")
    print("Hangi arama yöntemini kullanacaksınız?")
    cevap = int(input())
    if cevap == 1:
        index = LinearSearch(dizi, aranan)
    elif cevap == 2:
        index = JumpSearch(dizi, aranan, n)
    elif cevap == 3:
        index = BinarySearch(dizi, 0, len(dizi)-1, aranan)
    elif cevap == 4:
        index = interpolationSearch(dizi, n, aranan)
    elif cevap == 5:
        index = ExponentialSearch(dizi, n, aranan)
    else:
        print("Seçiminizi yeniden yapınız. Yaptığınız seçimi gerçekleştiremiyorum.\n")
        Chooser()
    return index

indexdonen = int(Chooser())
if indexdonen > -1:
    print(f"Dizi: {dizi}\nAranan İfade = {aranan}\nİfadenin İndexi = {indexdonen}\n")
else:
    print(f"Dizi: {dizi}\nAranan İfade = {aranan}\nİfade bulunamadı\n")
