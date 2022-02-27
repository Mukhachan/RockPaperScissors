import random
import sys

print("GAME")
print("Stones\Scissors\Paper")

opp=random.randint(1,3)

if opp==1:
    gg="Stone"
elif opp==2:
    gg="Scissors"
else:
    gg="Paper"
print("1) Stone")
print("2) Sccissors")
print("3) Paper")

a = input("start? (y/n) ")
while a == "y":
    try:
        x = int(input("Write the Number: \n>"))
        if x==1:
            print("")
            print("Your choise: Stone")
            print("Opponent choise: " +str(gg))
            print("")
            if opp ==1:
                print ("Draw:/*")
            elif opp==2:
                print ("You Win")
            else:
                print("Opponent win\n You lose")
            print("")

        elif x == 2:
            print("")
            print("Your choise: Scissors")
            print("Opponent choise: " + str(gg))
            print("")
            if opp == 1:
                print("opponent win\n You LOOOSE")
            elif opp == 2:
                print("Draw:/*")
            else:
                print("You Win")
                print("")
        elif x == 3:
            print("")
            print("Your choise: Paper")
            print("Opponent choise " + str(gg))
            print("")
            if opp == 1:
                print("You Win")
            elif opp == 2:
                print("opponent win")
            else:
                print("Draw:/*")
        else:
            print("Write only numbers")
        a = input("retry? (y/n) ")    
    except:
        print( "ERROR! Write only INT numbers" )

