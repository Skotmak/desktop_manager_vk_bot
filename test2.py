from random import randint

y = 1
print('y=0')
x = 1
print('x=1')
print('---------------')
while y == x:
    x = randint(0, 1000)
    print('x = ', x)
    y = 10
    print('y = ', y)
    print('no')
    print('---------------')
print('yes')