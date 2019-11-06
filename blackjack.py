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

if dealercalculate > 21:
    print("The dealer busted!")
    i = 0
if yourcalculate > 21:
    print("You busted!")
    i = 0

if dealercalculate < 21 and yourcalculate < 21:
    i = 1


def swap(hand):
    for i, x in enumerate(hand):
        if x == 11:
            hand[i] = 1

    return sum(hand)


while i == 1:
    print("Hit or Stand? Y or N")
    user_choice = input()
    if user_choice == 'y':
        yourhand.append(random.randrange(2, 12, 1))
        yourcalculate = sum(yourhand)
        print(yourhand)
        if yourcalculate > 21 and swap(yourhand) < 21:
            print("It seems you have 11 in your hand, would you like to switch to 1?")
            continue
        if yourcalculate > 21 and swap(yourhand) > 21:
            print("\n" + "You busted your ass")
            break
    elif user_choice == 'n':
        break
    else:
        print("please press y or n")
        continue

if yourcalculate <= 21:
    while dealercalculate < yourcalculate:
        dealershand.append(random.randrange(2, 12, 1))
        dealercalculate = sum(dealershand)
        print("Dealer will hit")
        print(dealershand)
        if dealercalculate > 21 and swap(dealershand) < 21:
            swap(dealershand)
            dealercalculate = sum(dealershand)
            continue
        if dealercalculate > 21 and swap(dealershand) > 21:
            print("Dealer busted after hitting! You won!!!")
            break

if dealercalculate < yourcalculate <= 21:
    print("\n" + "You won!")

if yourcalculate < dealercalculate <= 21:
    print("\n" + "The dealer won!")

if dealercalculate == yourcalculate:
    print("Tied!")

dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)

print('\n' + "Your total:")
print(yourcalculate)
print("Dealer's total:")
print(dealercalculate)

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