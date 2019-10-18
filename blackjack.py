import random

print("Welcome to Game of BlackJack")

dealershand = []
yourhand =[]

for x in range(0,2):
    dealershand.append(random.randrange(2,12,1))

for x in range(0,2):
    yourhand.append(random.randrange(2,12,1))

print("Here are you cards: ")
print (yourhand)

print("Here are the dealers card:")
print (dealershand)

dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)

i = 1
while i == 1:
    if dealercalculate < 20:
        print("Hit or Stand? Y or N")
        user_choice = input()
    if user_choice == 'y':
        yourhand.append(random.randrange(2, 12, 1))
        print (yourhand)
        break
    elif  user_choice == 'n':
        break
    else:
        print("please press y or n")
        continue
"""if dealercalculate > 21 & 11 in dealershand:
    print("Choose between 11 or 1")
    user choice = input()
    if :
"""
dealercalculate = sum(dealershand)
yourcalculate = sum(yourhand)

if dealercalculate > yourcalculate:
   print ("You suck ass")
else:
    if dealercalculate < yourcalculate:
        print ("Noice")
    else:
        print ("Draw, play again")

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

