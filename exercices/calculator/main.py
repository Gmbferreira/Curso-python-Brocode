import math

num1 = float(input ("Type the first number: "))
operator = input("Type your operator(+, -, *, /): ")
while operator not in ("+","-","*","/"):
    print ("invalid operator")
    operator = input("Type your operator(+, -, *, /): ")

num2 = float(input ("Type the second number: "))
response = 0

if operator == "+":
    response = num1 + num2
elif operator == "-":
    response = num1 - num2
elif operator == "*":
    response = num1 * num2
elif operator == "/":
    response = num1 / num2

print(response)
