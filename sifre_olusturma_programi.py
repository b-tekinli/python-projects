import random

print("\nŞİFRE OLUŞTURMA PROGRAMI\n")

chars = "abcçdefgğhiıjklmnoöprsştuüvyz0123456789.,?!#-_"
pw = ""
password = int(input("Parola kaç karakterli olsun?: "))
a = 1
while a <= password:
    number = random.randint(0, len(chars))
    pw += chars[number]
    a += 1
print(f"Şifreniz: {pw}")