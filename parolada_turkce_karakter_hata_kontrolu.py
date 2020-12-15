def checkPassword(parola):
     turkceKarakterler = "ığüşöçİ"

     for i in parola:
         if i in turkceKarakterler:
             raise TypeError("Parola türkçe karakter içeremez.")
         else:
             pass
     print("Geçerli parola.")

parola = input("Parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)