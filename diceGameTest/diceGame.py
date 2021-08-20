import random


def dice():
    number = random.randrange(1, 7)
    print(number)


again = True

ready = input(("are you ready to game? y/n :   "))
while again == True:
    if ready == "y":
        dice()
        ready2 = input(("do you want play again? y/n   "))
        if ready2 == "n":
            print("Thanks For Your Playing !!!")
            again = False
    elif ready == "n":
        print("Thanks For Your Playing !!!")
        again = False
    else:
        print("please Check Your Answer!!!")
