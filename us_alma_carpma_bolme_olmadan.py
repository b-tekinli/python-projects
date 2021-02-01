sayi1 = int(input("Üssü alınacak sayıyı giriniz: "))
sayi2 = int(input("Üssü giriniz: "))

if(sayi2 == 0):
    cevap = 1

cevap = sayi1
artisMiktari = sayi1

for i in range(1, sayi2):
    print("Adim:", i)
    print(artisMiktari, "+ (",end="")

    for j in range (1, sayi1):
        if j == (sayi1 - 1):
            cevap += artisMiktari
            print(artisMiktari, ")")
        else:
            cevap += artisMiktari
            print(artisMiktari, "+", end="")
    artisMiktari = cevap
    print("Bir sonraki adımda adımda artış miktarı", artisMiktari)
    
print(f"{sayi1} üzeri {sayi2} = {cevap}")