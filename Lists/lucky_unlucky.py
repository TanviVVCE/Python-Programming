x = 0
for i in range(1, 21):
    if (i == 4 or i == 13):
        x = 'Unlucky'
    elif (i % 2 == 0):
        x = 'Even'
    else:
        x = 'Odd'
    print(f'{i}: {x}')
