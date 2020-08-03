a = input("What is your name? ")
if a == "bob":
    print("Hi, bob")
elif a == "Akshaya":
    print("Hi, Akshaya")
else:
    print("Hello")

age = int(input("Enter your age: "))
if age <= 4:
    print("Your ticket cost is $0")
elif age < 18 and age > 4:
    print("Your ticket cost is $10")
else:
    print("Your ticket cost is $15")
