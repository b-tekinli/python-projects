print("\nFİZZBUZZ PROGRAMI\n")

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

length = int(input("Dizi uzunluğunu giriniz: "))

for a in range(1, length):
    print(fizzbuzz(a))