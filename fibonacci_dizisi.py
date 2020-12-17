print("\nFİBONACCİ\n")

print("Fibonacci Nedir?\nKendisi ve öncesindeki sayının toplamına eşittir. İlk iki hanesi 0 ve  1’dir. Bu sayılar birbirine oranlandığında altın oran çıkmaktadır.")

def fibonacci(hesapla):
    number1 = 0
    number2 = 1
    print(f"{number1} + {number2} = ",number1+number2)
    for i in range(0,11):
        number3 = number1 + number2
        print(number3)
        number1 = number2
        number2 = number3
hesapla = int(input("\nSayı giriniz: "))
fibonacci(hesapla)