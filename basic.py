print("Hello")
a=float(input("Enter radius:"))

print(f"Area:{3.14**a}")

#List
fruits = ["Apple","Orange","lichi"]
fruits.append("guava")
print(fruits)

#Tuple
fruits = ("apple","orange")
fruits.append("banana")
print(fruits)

#Dictionary
employee = {"Name":"vimal","age":23}
print(employee["age"])

# Set
num = {1,2,3,4,5,4,2,3}
num.add(7)
print(num)

#if-else LOOP
age = int(input("Enter your age:"))
if age<18:
    print("Minor,Not eligible")
elif age==18:
    print("Eligible")
else:
    print("Eligible")

# FOR LOOP 

fruits = ["apple","banana","orange"]
for i in fruits:
    print(i,end=" ")

for i in range(1,22):
    if i%7==0:
        print(i,end=" ")

for i in range(1,22,2):
    print(i,end=" ")

students = {"rahul":67, "rohan":89, "Kiran":97, "athul":91}
for student,marks in students.items():
    if marks>90:
        print(student,marks)

list = [23,12,5,76,93,16]
largest = list[0]
for num in list:
    if num>largest:
        largest=num
print(largest)

#Lambda function
division = lambda x,y: x/y
print(division(6,3))

#a = int(input("Enter a number:"))
# if a%2 == 0:
#     print("Even")
# else:
#     print("Odd")

#Factorial
fact=1
for i in range(1,a+1):
    fact = fact*i
print(fact)
flag=1
if a<2:
    print("Not prime")
    exit()
for i in range(2,a//2+1):
    if a%i==0:
        flag=0
        break
if flag == 0:
    print("Not prime")
else:
    print("Prime")

#Count frequency of letters
a = input("Enter a string:")
dict = {}
for i in a:
    if i !=" ":
        dict[i] = dict.get(i,0)+1
print(dict)
