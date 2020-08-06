num = int(input("Enter a number: "))
temp = True
for x in range(2, num):
    if num % x == 0:
        print("%s is a composite" % num)
        temp = False
        break
if temp:
    print("%s is a prime" % num)
