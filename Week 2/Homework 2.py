dct = {}

f_name = input("Enter your first name: ")
dct['First Name'] = f_name
l_name = input("Enter your last name: ")
dct['Last Name'] = l_name
age = int(input("Enter your age: "))
dct['Age'] = age
city = input("Enter the city you live in: ")
dct['City'] = city

print("These are the keys: ")
for n in dct:
    print(n)

print("These are the values: ")
for x in dct.values():
    print(x)

print("These are the items:")
for y in dct.items():
    print(y)
