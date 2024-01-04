import random
response = "y"
while response=="y":
    randomnum = random.randint(1,6)
    if randomnum == 1:
        print('---')
        print('-*-')
        print('---')
    elif randomnum == 2:
        print('---')
        print('-**')
        print('---')
    elif randomnum == 3:
        print('--*')
        print('-*')
        print('*--')
    elif randomnum == 4:
        print('*-*')
        print('---')
        print('*-*')
    elif randomnum == 5:
        print('*-*')
        print('-*-')
        print('*-*')
    elif randomnum == 6:
        print('*-*')
        print('*-*')
        print('*-*')
    userInput = (input("Do you want to roll a dice?"))
