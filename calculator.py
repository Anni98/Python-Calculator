# This is A simple calculator

print("Welcome to Basic Calcualtor..!")
a = int(input("First Number You Wanna Procced With:"))
b = int(input("Second Number You Wanna Procced With:"))
c = input("You wanna do with them? (+,-,*,/): ")

if c == "+":
    print("Result:", a+b)
elif c == "-":
    print("Result",a-b)
elif c == "*":
    print("Result:",a*b)
elif c == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation! Please choose add, subtract, multiply, or divide.")
print("Your calculation is solved.. Please Come Back")

#End Of Calcualtor
