# first_messages = input('Hey hows its going ?')
# messages = ''
# while first_messages != 'stop copying me':
#     if (first_messages == 'stop copying me'):
#         messages = 'stop copying me'
#     else:
#         print(first_messages)
#         first_messages = input()
#         messages = first_messages
# print('UGH FINE YOU WIN')

msg = input('Hey hows its going ?')
while msg != 'stop copying me':
    msg = input(f'{msg}')
print('UGH FINE YOU WIN')
