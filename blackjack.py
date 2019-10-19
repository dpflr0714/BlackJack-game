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

if dealercalculate == 21:
    print("Dealer got blackjack")

while dealercalculate < 18:
        dealershand.append(random.randrange(2,12,1))
        for i, x in enumerate(dealershand):
            if x == 11:
                dealershand[i] = 1
                dealercalculate = sum(dealershand)




print("Here are you cards: ")
print(yourhand)

print("Here are the dealers card:")
print(dealershand)


i = 1
while i == 1:
    if dealercalculate < 21 and yourcalculate < 21:
        print("Hit or Stand? Y or N")
        user_choice = input()
    if user_choice == 'y':
        yourhand.append(random.randrange(2, 12, 1))
        print(yourhand)
        if yourcalculate <= 21:
            i = 1
        else:
            print("You busted your ass son")
    elif user_choice == 'n':
        break
    else:
        print("please press y or n")
        continue






dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)

if dealercalculate > yourcalculate:
   print("You suck ass")
else:
    if dealercalculate < yourcalculate:
        print("Noice")
    else:
        print("Draw, play again")

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

