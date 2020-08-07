fruits = ['pineapple', 'watermelon', 'kiwi', 'orange',
          'apple', 'banana', 'grapes', 'orange', 'watermelon',
          'orange']
print(fruits)
print(fruits[4])
del fruits[2]
fruits.remove('pineapple')
print(fruits)
fruits.append('pineapple')
fruits.insert(2,'kiwi')
print(fruits)
for x in fruits:
    print(x)