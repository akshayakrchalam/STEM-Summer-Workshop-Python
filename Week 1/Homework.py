def add():
    print("The sum of %d and %d is %d" % (num_1, num_2, num_1 + num_2))

def sub():
    print("The difference of %d and %d is %d" % (num_1, num_2, num_1 - num_2))

def mul():
    print("The product of %d and %d is %d" % (num_1, num_2, num_1 * num_2))

def div():
    print("The quotient of %d and %d is %d" % (num_1, num_2, num_1 / num_2))

def rem():
    print("The remainder of %d and %d is %d" % (num_1, num_2, num_1 % num_2))

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
add()
sub()
mul()
div()
rem()

n_1 = 5
n_2 = 10
add = n_1 + n_2
print("The sum of {} and {} is {}".format(n_1, n_2, add))