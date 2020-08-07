makes = ['honda','tesla','toyota']
car = {'make':makes, "model":"model s", "year": 2020}
print(car)
print(car['year'])
del car['model']
print(car)
car['model'] = 'model s'
print(car)
car['model'] = 'model x'
print(car)
for x in car:
    print(x)
for y in car.values():
    print(y)
for x,y in car.items():
    print("{} : {}".format(x,y))
