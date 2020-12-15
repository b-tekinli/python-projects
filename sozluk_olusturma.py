sozluk = {
    "book" : "kitap",
    "table" : "masa"
    }

sozluk2 = dict(kitap = "book", masa = "table")

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
del(sozluk["book"])
print("Kaç kelime var: ",len(sozluk),"\n","Kelimeler: ",sozluk2)