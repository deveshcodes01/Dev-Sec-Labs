# q1
def welcome():
    print("hello world")
welcome()

# q2
def bio(name="devesh"):
    print("hello",name)
bio()

# q4
def sq(num):
    print(num*num)
sq()

# q5

# q6
def find_max(n1,n2):
    if(n1>n2):
        print(n1)
    else:
        print(n2)
find_max(10,20)

# q7
def print_list():
    l1=input["enter numbers"]

# # q11
def calculate_SI(p,t,r=0.05):
    int=p*r*t
    return int

int1=calculate_SI(1000,2)

# q12
def display_info(name,age):
    print("name",name)
    print("age",age)
display_info(age=22,name="amit")

# q13
def find_sum(*args):
    return sum(args)
print("sum: ",find_sum(10,20,30,40))

# q14
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_info(name="rahul",age=20,city="lucknow")

# q15