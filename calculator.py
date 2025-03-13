# This is A simple calculator

print("Welcome to Basic Calcualtor..!")
a = int(input("First Number You Wanna Procced With:"))
b = int(input("Second Number You Wanna Procced With:"))
c = input("You wanna do with them? (+,-,*,/,sq,cube,Raise): ")
d = a*a
e = a**3

if c == "+":
    print("Result:", a+b)
elif c == "-":
    print("Result",a-b)
elif c == "*":
    print("Result:",a*b)
elif c == "sq":
    print(f"Square is is {d}")
elif c == "cube":
    print(f"Result is {e}")
elif c == "Raise":
    raiser = int(input("Raise to the power of?: "))
    print(f"Result is {a**raiser}")
elif c == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation! Please choose add, subtract, multiply,divide,or Other FUnctions.")
print("Your calculation is solved.. Please Come Back")

#End Of Calcualtor