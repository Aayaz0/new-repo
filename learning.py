"""Aaaba python sabai sikna parxa
Day one  lesson one
"""


from detail import detail
detail=detail("Jiban","Shrestha","Iam studing in texas college")
print(detail.firstname,detail.secondname)


number1= 20
number2=30
print(f"The result is {number1 + number2}")
print(f"The result is {number1 * number2}")

previous_number =0
for i in range (0,11):
    print(f"current number {i} and previous number {previous_number} sum is {i +previous_number}")

str="PYnative"
print(len(str))
str = str.replace("n","")# string ma direct remove garna mildaina list ma jasto
print(str)

print(str[0])
print(str[2])
print(str[4])
print(str[6])



list = [10,20,33,46,55]
for i in list:
    if i%5==0:
        print(i)


list1 =[10,20,25,30,35]
list2 =[40,45,60,75,90]
list1.extend(list2)
print(list1)
list1.append(list2)
print(list1)


for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


