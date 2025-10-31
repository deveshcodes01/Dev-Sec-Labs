num=[10,20,30,40,50]
n=int(input("enter a number to check "))
if n in num:
    print(f"{n} exist in the list ")
else:
    print(f"{n} does not exist in the list ")

print(num.index(30))
