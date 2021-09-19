from builtins import print

from Balance import *


play = True
print("Welcome from Golden City's Gambling App")
while play:
    print('Your Current point is {}'.format(balance))

    # Check the balance
    if balance == 0:
        # Asking the player if he/she is willing to top up
        check = input('Do you want to top up? Y?N : ')
        check = check.upper()
        print(check)
        if check == 'Y':
            balance = topup()

    num = 0
    while num < 1 or num > 6:
        num = input("Predict a number between 1~6 : ")
        num = int(num)

    available = False
    while available == False:
        # Checking if the player have enough points to play
        point = input("Enter the point you want to bet : ")
        point = int(point)
        if point > balance:
            print("You don't have enough points.")
        else:
            available = True

    # Updating the balance
    balance = balance + bet(point, num)
    print("Your current point is : {}".format(balance))

    kon = True
    while kon:
        kontinue = input("Do you want to play again? Y?N : ")
        kontinue = kontinue.upper()
        if kontinue == 'N':
            play = False
            kon = False
            print("Your total cash is : {}".format(balance))
            print("Good Bye")
        elif kontinue == 'Y':
            kon = False
        else:
            print("Incorrect input !")
