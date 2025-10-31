import random
chars="abcdefghilklmnopqrstuvwxyzABCDEFGHIJKLMNOPARSTUVWXYZ!@#$%^&*()"
len=int(input("enter length: "))
password=" "

for a in range(len):
    password+=random.choice(chars)
print(password) 