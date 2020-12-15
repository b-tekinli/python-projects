# 1. Soru:
ogrenciler = {}

number = input("Öğrenci No: ")
name = input("Öğrenci Ad: ")
surname = input("Öğrenci Soyad: ")
phone = input("Öğrenci Telefon: ")

ogrenciler[number] = {
        "ad": name,
        "soyad": surname,
        "telefon": phone
}

print(ogrenciler)

ogrenciler.update({
       number: {
          "ad": name,
           "soyad": surname,
           "telefon": phone

       }
})