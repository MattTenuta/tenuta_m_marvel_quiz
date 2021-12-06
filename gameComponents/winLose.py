from gameComponents import gameVars

def avengerStatus():        
    print("==============================")
    print("Your total Avenger Points are: " + str(gameVars.avengerPoints))

    if gameVars.avengerPoints == 0:
        print("You are not worthy of the Avenger title. Get out of my sight")

    elif gameVars.avengerPoints == 1:
        print("You are not even 1% Avenger")
    
    elif gameVars.avengerPoints == 2:
        print("Not even close. You probably like DC more than marvel")

    elif gameVars.avengerPoints == 3:
        print("You are barely an Avenger")
            
    elif gameVars.avengerPoints == 4:
        print("I guess you can be considered an Avenger")

    elif gameVars.avengerPoints == 5:
        print("You are the chosen one. A true Avenger is upon us")

        print("==============================")
        print("Thanks you for playing")

    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("Gone, Reduced to Atoms")
        exit()
    elif choice == "y":
        print("==============================")
        print("Awesome! Lets Play!")
        player = False
