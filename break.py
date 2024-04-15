# while 1:
#     msg = input('Type \'exit\' to escape')
#     if (msg == 'exit'):
#         break

from random import randint
number = randint(1, 10)
while number != 5:
    print(number)
    number = randint(1, 10)
    if (number == 5):
        break
