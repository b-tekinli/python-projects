print("\nTAM BÖLENLERİ BUL\n")

def tamBolenleriBul (sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler
print(tamBolenleriBul(20))