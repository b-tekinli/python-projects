try:
    sayi = int(input("Sayı giriniz: "))
except ValueError:
    print("Tip uyuşmazlığı : Lütfen sayı giriniz")
except ZeroDivisionError:
    print("Payda sıfır olamaz.")
except:
    print("Bir hata oluştu.")
    
print("Bitti.")