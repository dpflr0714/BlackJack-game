import random

print("***************************************Welcome to Game of BlackJack***************************************")
i = 1
dealershand = []
yourhand =[]

for x in range(0,2):
    dealershand.append(random.randrange(2,12,1))

for x in range(0,2):
    yourhand.append(random.randrange(2,12,1))

dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)

print("Here are your cards: ")
print(yourhand)

print("Here are the dealers card:")
print(dealershand)


if dealercalculate < 21 and yourcalculate < 21:
    i = 1

while i == 1:
    print("Hit or Stand? Y or N")
    user_choice = input()
    if user_choice == 'y':
        yourhand.append(random.randrange(2, 12, 1))
        yourcalculate = sum(yourhand)
        print(yourhand)
    elif user_choice == 'n':
        break
    elif yourcalculate > 21:
        print("You busted your ass")
        break
    else:
        print("please press y or n")
        continue


if yourcalculate < 21:
    dealershand.append(random.randrange(2, 12, 1))
    dealercalculate = sum(dealershand)
    print("Dealer will hit")
    print(dealershand)
    if dealercalculate > yourcalculate:
        print("Congrats, you won!")
    elif dealercalculate == yourcalculate:
        print("Tied")
    else:
        print("Sorry you lost")


dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)


"""
if dealercalculate < yourcalculate:
    print("Congrats, you won!")
elif dealercalculate == yourcalculate:
    print("Tied")
else:
    print("Sorry, you lost")
"""

def swap(hand):
    for i, x in enumerate(hand):
        if x == 11:
            hand[i] = 1


swap(yourhand)
swap(dealershand)




print(dealercalculate)
print(yourcalculate)














#if dealershand

"""cardlist = ['K','Q','J','A']

def units():
    mapping = {
        'K' : 10,
        'Q' : 10,
        'J' : 10,
        'A' : 1
    }

if ()
    return 1
else:
    return 11
"""

