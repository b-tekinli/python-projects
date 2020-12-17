print("\nEHLİYET UYGULAMASI\n")

ad = input("Ad: ")
yas = int(input("Yaş: "))
egitim = input("Eğitim: ")

if (yas >= 18):
    if (egitim == "lise" or egitim == "üniversite"):
        print(f" {ad} ehliyet alabilirsin.")
    else:
        print(f" {ad} ehliyet alamazsın eğitim durumun yetersiz.")
else:
    print(f" {ad} ehliyet alamazsın yaşın tutmuyor.")