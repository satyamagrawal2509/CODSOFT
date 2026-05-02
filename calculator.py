a = float(input("enter first number: "))
b = float(input("enter second number: "))

op = input("enter operation (+ - * /): ")

if op == "+":
    print(a + b)

elif op == "-":
    print(a - b)

elif op == "*":
    print(a * b)

elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("cannot divide by 0")

else:
    print("wrong operation")
