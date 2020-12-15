print("\nORTALAMA HESAPLAMA PROGRAMI")

vize = float(input("Vize: "))
final = float(input("Final: "))
but = float(input("Büt: "))

ort = (((vize + final) / 2) * 0.6) + (but * 0.4)

print(f"not ortalamanız: {ort} ve dersten geçme durumunuz: {ort>=50}")