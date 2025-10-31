students = [{"name": "amit", "age": 20}, {
    "name": "neha", "age": 22}, {"name": "rahul", "age": 19}]
print(students[0,"name"])
for i in students:
    print(i["name"])

students.append({"name":"priya","age":21})
print(students)

students[2]["age"]=20
print(students)

for student in students:
    if student["age"] == 22:
        print("oldest")
    else:
        print("eldest")
s1 = dict[students]
print(s1)
