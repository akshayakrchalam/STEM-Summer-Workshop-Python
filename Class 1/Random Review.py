while True:
    num = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    total = num + num2
    print(total)
    q = input("Do you want to quit? ")
    if q == "yes":
        break
print("hi")
x = 1
y = 2
print(x)
print(y)
x += y
print(x)
print("Hi %d bye %d" % (x, y))
print("Hi %d bye %d" % (y, x))
a = input("Enter a number: ")
print(a)
for x in range(0, 20):
    print(x)
if x == 19:
    print("x has been printed")
while x > 0:
    print("Python")
    x -= 1
if x == 0:
    print("Python has been printed")
