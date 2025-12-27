# calculator program

operator = input("Enter any Operator (+, -, *, /):   ")

num1 = int(input("Enter The 1st number:  "))
num2 = int(input("Enter The 2nd number:  "))

if operator == "+":
    result = (num1 + num2)
    print(f"The addition of {num1} and {num2} is {result}")
elif operator == "-":
    result = (num1 - num2)
    print(f"The subraction of {num1} and {num2} is {result}")
elif operator == "*":
    result = (num1 * num2)
    print(f"The multiplication of {num1} and {num2} is {result}")
elif operator == "/":
    result = (num1 / num2)
    print(f"The Division of {num1} and {num2} is {result}")
else:
    print(f"{operator} is not a operator")
