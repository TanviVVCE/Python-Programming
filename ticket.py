age = input("Whats your age ?\n")

if age != '':
    if (int(age) >= 18):
        if (int(age) >= 21):
            print("Yipee !! you can have drinks")
        else:
            print("Wristbands Only")
    else:
        print('Waie till you get 18 !!')
else:
    print('I am still being trained please provide proper inputs')
