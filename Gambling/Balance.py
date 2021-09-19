from random import *

# balance of the player
balance = 0


# Top up to be able to play the game
def topup():
    topup = int(input("Enter the amount you want to top-up : "))
    balance = topup + (topup / 10)
    print('Your current point is {}'.format(balance))
    return balance


# Betting function
def bet(point, num):
    rnum = randint(1, 6)
    print("The number is {}".format(rnum))
    if num == rnum:
        print("Congratulations! You won.")
        point = point * 1
    else:
        print("Sorry, you've lost.")
        point = point * -1
    return point
