import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"
symbols = "!@#$%^&*()_+"

all_chars = letters + nums + symbols

n = int(input("enter password length: "))

pwd = ""

for i in range(n):
    ch = random.choice(all_chars)
    pwd = pwd + ch

print("your password is:", pwd)
