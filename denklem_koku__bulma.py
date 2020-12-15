import math

a = int(input("Lütfen A katsayısını giriniz: "))    # 3. 4. ve 5. satırlarda a, b ve c katsayılarını kullanıcıdan istedik.
b = int(input("Lütfen B katsayısını giriniz: "))
c = int(input("Lütfen C katsayısını giriniz: "))

delta = b**2 - (4*a*c)                              # Delta hesaplayan formülü delta değişkenine atadık.
print("Delta =",delta)                              # Deltayı ekrana yazdırdık.

if delta < 0:                                       # Deltanın 0'dan küçük olması koşulunu belirttik.
    print("Denkleminizin reel kökü yoktur.")        # Koşul sağlandığında ekrana yazılacak metinsel ifadeyi yazdırdık.

elif delta == 0:                                    # 2. koşulumuzu deltanın 0'a eşit olması durumu için belirttik.
    x = (-b / (2*a))                                # Bulacağımız kökün formülünü x değişkenine atadık.
    print(f"Kök: {x}")                              # Bulduğumuz kök sonucunu ekrana yazdırdık.
    print("Denkleminizin eşit 2 kökü vardır.")      # Sonuca göre denklem hakkında bilgiyi ekrana yazdırdık.

else:                                                   # Deltanın 0'dan büyük olması koşulunu belirttik.
    x1 = (-b - math.sqrt(delta)) / (2 * a)              # 1. kökü hesaplatan formülü x1 değişkenine atadık.
    x2 = (-b + math.sqrt(delta)) / (2 * a)              # 2. kökü hesaplatan formülü x2 değişkenine atadık.
    print(f"Denkleminizin 1. kökü: {x1}\nDenkleminizin 2. kökü: {x2}")     # Denklemin köklerini ekrana yazdırdık.
    print("Denkleminizin iki farklı reel kökü vardır.")                    # Sonuca göre denklem hakkında bilgiyi ekrana yazdırdık.