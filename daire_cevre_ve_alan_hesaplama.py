class Circle:
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()} ")
print(f"c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()} ")


# pi = 3.14
# r = float(input("Yarıçapı giriniz: "))
# alan = pi * (r ** 2)
# cevre = 2 * pi * r
# print("alan: ",alan)
# print("çevre: ",cevre)