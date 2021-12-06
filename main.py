from gameComponents import gameVars, winLose

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
        print("==============================")
        print("Awesome! Lets Play!")
        player = False

while player is False:
        gameVars.avengerPoints = 0
        print("Here is your first question")
        print("==============================")
        Q1 = input("What superhero was created as a super soldier to fight in WW2? Was it a) Iron Man, b) Captain America, c) The Hulk, or d) Black Widow ")

        if Q1 == "b":
                print("Good Job, Maybe you are an Avenger?")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))
        else:
                print("You are Wrong. Are you sure you are a marvel fan?")
                print("No avenger points for you, Dirtbag")
                print("Avenger Points: " + str(gameVars.avengerPoints))
        
        print("==============================")
        print("Next Question")
        print("==============================")
        Q2 = input("What Avenger graduated from MIT with multiple degrees when they were 21 years old? Was it a) Hawkeye, b) Spiderman, c) Iron Man, or d) Thor ")
        
        if Q2 == "c":
                print("Woah, yout got that right? I guess there is a brain in that head of yours")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))
        else:
                print("You are Wrong. Are you even trying?")
                print("No avenger points for you, Dirtbag")
                print("Avenger Points: " + str(gameVars.avengerPoints))
        
        print("==============================")
        print("Next Question")
        print("==============================")
        Q3 = input("What marvel character was trained as a lethal sleeper agent for the Soviet Union? Is it a) Groot, b) Ant-Man, c) Black Panther, or d) Black Widow ")
        
        if Q3 == "d":
                print("Congratulations, You go it right. You must be cheating right?")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))
        else:
                print("Damn, you really suck at this.")
                print("No avenger points for you, Dirtbag")
                print("Avenger Points: " + str(gameVars.avengerPoints))

        print("==============================")
        print("Next Question")
        print("==============================")
        Q4 = input("This marvel character is from the planet Titan and they killed their whole family. Was it a) Green Goblin, b) Loki, c) Thanos, or d) Nick Fury ")
        
        if Q4 == "c":
                print("How did you even know that? You need to calm down a little")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))
        else:
                print("Wow, you really got that one wrong?")
                print("No avenger points for you, Dirtbag")
                print("Avenger Points: " + str(gameVars.avengerPoints))
        
        print("==============================")
        print("Next Question")
        print("==============================")
        Q5 = input("What marvel character is a master strategist and problem solver who is an expert in close-quarter combat, various human and alien firearms, and battle techniques? Is it a) Groot, b) Star Lord, c) Doctor Strange, or d) Captain Marvel ")
        
        if Q5 == "b":
                print("Great Work, You are amazing!")
                gameVars.avengerPoints = gameVars.avengerPoints + 1
                print("Avenger Points: " + str(gameVars.avengerPoints))

        else:
                print("We are just going to ignore that you got that wrong")
                print("No avenger points for you, Dirtbag")
                print("Avenger Points: " + str(gameVars.avengerPoints))
                
        winLose.avengerStatus()
      
