import random
 
pc=random.randint(1,50)

me=0
sayi=1
while pc!=me:
  me=int(input("Tahmin ettiğim sayıyı gir: "))

  if me==pc:
    #print("{} tahminde bildin".format(say))
    print(sayi,". tahminde bildiniz")
  elif me>pc:
    print("Daha küçük bir sayı dene")
  else:
    print("Daha büyük bir sayı dene")
  sayi+=1