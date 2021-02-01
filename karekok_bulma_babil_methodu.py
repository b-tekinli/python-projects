sayi= int(input("Karekökü alınacak sayı: "))
e = float(input("Doğruluk seviyesi(Ne kadar küçükse o kadar iyi): "))
x = sayi
y = 1
while(x - y > e):
    x = (x + y) / 2
    y = sayi / x
print(f"{sayi} sayısının karekökü = {x}, doğruluk seviyesi= {e}")