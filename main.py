from gameComponents import gameVars

print("==============================")
print("Welcome to my Marvel character quiz made using python")
print("==============================")
print("Follow these simple rules if you want to survive")
print("You will be asked a question about a Marvel character and you must provide the correct answer")
print("For each correct anser you will earn 1 Avenger Point")
print("At the end, the computer will determine if you are a real Avenger or not")
print("And one other thing, when typing your answers, use lower case letters or it will not work")
print("==============================")

choice = input("Do you want to play? y/n: ")

if choice == "n":
        print("Gone, Reduced to Atoms")
        exit()
elif choice == "y":
        print("Awesome! Lets Play!")
        player = False

while player is False:
        print("Here is your first question")
        print("==============================")
        Q1 = input ("What superhero was created as a super soldier to fight in WW2? Was it a) Iron Man, b) Captain America, c) The Hulk, or d) Black Widow ")

        if Q1 == "b":
                print("Good Job, Maybe you are an Avenger?")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))
        else:
                print("You are Wrong. Are you sure you are a marvel fan?")
                print("No avenger points for you, Dirtbag")


                
























