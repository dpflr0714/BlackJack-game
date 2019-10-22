import random

print("***************************************Welcome to Game of BlackJack***************************************")

dealershand = []
yourhand =[]

for x in range(0,2):
    dealershand.append(random.randrange(2,12,1))

for x in range(0,2):
    yourhand.append(random.randrange(2,12,1))

dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)



def dealerplay():
if 17 < dealercalculate < 21:
    i = 1
elif dealercalculate < 17:
    while dealercalculate < 17:
        dealershand.append(random.randrange(2,12,1))
        dealercalculate = sum(dealershand)
        for i, x in enumerate(dealershand):
            if x == 11:
                dealershand[i] = 1
                dealercalculate = sum(dealershand)
                i = 1

elif dealercalculate <
else:
    print("***Dealer got 21***")
    i = 0

print("Here are your cards: ")
print(yourhand)

print("Here are the dealers card:")
print(dealershand)


while i == 1:
    if yourcalculate < 21:
        print("Hit or Stand? Y or N")
        user_choice = input()
        if user_choice == 'y':
            yourhand.append(random.randrange(2, 12, 1))
            print(yourhand)
        elif user_choice == 'n':
            break
    elif yourcalculate > 21:
        print("You busted your ass")
    else:
        print("please press y or n")
        continue






dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)


# Need to check for 11 on players' deck and give a choice of 11 or 1
# If dealer goes over 21, it becomes a bust
# The player wins as long as its greater than dealer regardless of going over 21, need to fix













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

