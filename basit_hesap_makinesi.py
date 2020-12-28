import math

print("CALCULATOR\n")

one = "Addition"
two = "Extraction Operation"
three = "Multiplication"
four = "Division"
five = "Exponentiation"
six = "Operation of Getting Mod"
seven = "Square Root Operation"
eight = "Quit"
operation = "Choose the operation you want to do: "

while True:
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    choose = int(input(f"1.{one}\n2.{two}\n3.{three}\n4.{four}\n5.{five}\n6.{six}\n7.{seven}\n8.{eight}\n{operation}"))
    if choose == 1:
        print("Result = ",number1 + number2)
    elif choose == 2:
        print("Result = ",number1 - number2)
    elif choose == 3:
        print("Result = ",number1 * number2)
    elif choose == 4:
        while not number2:
            number2 = int(input("Please enter a number other than zero -0-: "))
        print("Result = ",number1 / number2)
    elif choose == 5:
        print("Result = ",number1 ** number2)
    elif choose == 6:
        print("Result = ",number1 % number2)
    elif choose == 7:
        print("Result = ",math.sqrt(number1),"and", math.sqrt(number2))
    elif choose == 8:
        print("Signing out...")
        break
    else:
        print("You entered an invalid transaction, try again.")

        