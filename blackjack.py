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


if 18 < dealercalculate < 21:
    i = 2

elif dealercalculate < 18:
    dealershand.append(random.randrange(2,12,1))
    dealercalculate = sum(dealershand)
    for i, x in enumerate(dealershand):
        if x == 11:
            dealershand[i] = 1
            dealercalculate = sum(dealershand)
            i = 1


while i == 1:
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

if dealercalculate < yourcalculate:
    print("Congrats, you won!")
elif dealercalculate == yourcalculate:
    print("Tied")
else:
    print("Sorry, you lost")





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

