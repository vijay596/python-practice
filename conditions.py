x = 2
print(x == 2)
print( x == 3)
print(x < 3)
print("----------------------------")


name = 'john'
age = 23
if name == 'john' and age == 23:
    print (f'your name is {name}, and your age also {age} years')

if name == 'john' or name == 'vijay':
    print('your name is either john or vijay')
print('-------------------------------------------------------------------------------')


x = 2
if x == 2:
    print('x is equals two')
else:
    print("x doesn't equals to 2")

print('---------------------------------------------')

statement = False
another_statment = True
if statement is True:
    print('statement is True')
elif another_statment is False:
    print('another_statment is True')
else:
    print('not satisfied')

print('-------------------------------------------')

#not operator
print(not True)
print((not False) == False)

print('----------------------')

#Exercise
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print('1')
if first_array:
    print('2')
if len(second_array) == 2:
    print('3')
if len(first_array) + len(second_array) == 5:
    print('4')
if first_array and first_array[0] == 1:
    print('5')
if not second_number:
    print('6')