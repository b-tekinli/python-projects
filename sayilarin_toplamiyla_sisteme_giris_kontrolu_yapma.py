import random                                               # Random kütüphanesini içeri aktararak aktifleştirdik.

number1 = random.randrange(10, 100)                         # Bilgisayarın ilk sayıyı rastgele vermesi için number1 değişkenine atadık.
print(f"Sayı: {number1}")                                   # İlk sayıyı ekrana f string kullanarak yazdırdık.

number2 = random.randrange(0, 10)                           # Bilgisayarın ikinci sayıyı rastgele vermesi için number2 değişkenine atadık.
print(f"Sayı: {number2}")                                   # İkinci sayıyı ekrana f string kullanarak yazdırdık.

addition = number1 + number2                                # Tanımladığımız 2 sayının toplamını addition değişkenine atadık. 

result = int(input("Sayıların toplamını giriniz: "))        # Kullanıcıdan sayıların toplamını girmesini istedik.

if addition == result:                                      # addition ve result değişkenlerinin birbirine eşit olması koşulunu belirttik.
    print("Cevabınız doğru. Sisteme giriş başarılı.")       # Belirttiğimiz koşul sağlandığında ekrana, verdiğimiz mesaj yazdırılır.
else:                                                       # İlk koşulumuz sağlanmazsa ona zıt olarak çalışacak olan şartı belirttik.
    print("Cevabınız yanlış. Lütfen tekrar deneyiniz..")    # Koşul sağlandığında ekrana verdiğimiz mesaj yazdırılır.