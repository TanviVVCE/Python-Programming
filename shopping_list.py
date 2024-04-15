print('!! WELCOME TO YOUR SHOPPING CART !!')
shopping_list = []
while True:
    shopping_item = input('Add something to the cart? Type q to quit: ')
    shopping_list.append(shopping_item)
    if (shopping_item == 'q'):
        break
print('\nYour final grocery list: \n')
for i in shopping_list:
    if (i == 'q'):
        break
    print(f'-- {i}')
