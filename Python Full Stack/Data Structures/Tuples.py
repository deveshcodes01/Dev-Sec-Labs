# t=(3,4,5,6,7)
# print(t[0])
# print(t[-1])
# print(len(t))

# SEARCHING

num=(10,20,30,40,50)
n=int(input("enter a number to check "))
if n in num:
    print(f"{n} exist in the tuple ")
else:
    print(f"{n} does not exist in the tuple ")

print(num.index(30))
