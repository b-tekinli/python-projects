print("\nÜRÜNLER\n")

urunler = []
adet = int(input("Kaç adet ürün eklemek istiyorsunuz? "))
a = 0

while (a < adet):
    name = input("Ürün ismi: ")
    price = input("Ürün fiyatı: ")
    urunler.append({
        "name": name,
        "price": price
    })
    a += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')