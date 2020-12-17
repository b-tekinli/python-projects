import math

print("\nSİLİNDİR HACMİ HESAPLAMA")

def silindir(pi, yarıçap, yükseklik):
    hacim = pi * yarıçap ** 2 * yükseklik
    print(hacim)

print()
silindir( 2, 4, 12)