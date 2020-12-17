print("\nKARNE NOTU HESAPLAMA\n")

not1 = float(input("1. Not: "))
not2 = float(input("2. Not: "))
sozlu = float(input("Sözlü: "))

ort = (not1 + not2 + sozlu) / 3

if (ort >= 0) and (ort < 25):
    print(f"ortalamanız: {ort} notunuz: 0")
elif (ort >= 25) and (ort < 45):
    print(f"ortalamanız: {ort} notunuz: 1")
elif (ort >= 45) and (ort < 55):
    print(f"ortalamanız: {ort} notunuz: 2")
elif (ort >= 55) and (ort < 70):
    print(f"ortalamanız: {ort} notunuz: 3")
elif (ort >= 70) and (ort < 85):
    print(f"ortalamanız: {ort} notunuz: 4")
elif (ort >= 85) and (ort < 100):
    print(f"ortalamanız: {ort} notunuz: 5")
else:
    print("Yanlış bilgi girdiniz.")