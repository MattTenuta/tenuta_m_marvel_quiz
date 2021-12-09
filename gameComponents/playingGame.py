from gameComponents import gameVars, winLose

def game():
    gameVars.avengerPoints = 0
    print("Here is your first question")
    print("==============================")
    Q1 = input("What superhero was created as a super soldier to fight in WW2? Was it a) Iron Man, b) Captain America, c) The Hulk, or d) Black Widow ")

    if Q1 == "b":
        print("==============================")
        print("Good Job, Maybe you are an Avenger?")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("You are Wrong. Are you sure you are a marvel fan?")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))
        
    print("==============================")
    print("Next Question")
    print("==============================")
    Q2 = input("What Avenger graduated from MIT with multiple degrees when they were only 21 years old? Was it a) Hawkeye, b) Spiderman, c) Iron Man, or d) Thor ")
        
    if Q2 == "c":
        print("==============================")
        print("Woah, yout got that right? I guess there is a brain in that head of yours")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("You are Wrong. Are you even trying?")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))
        
    print("==============================")
    print("Next Question")
    print("==============================")
    Q3 = input("What Marvel character was trained as a lethal sleeper agent for the Soviet Union? Was it a) Groot, b) Ant-Man, c) Black Panther, or d) Black Widow ")
        
    if Q3 == "d":
        print("==============================")
        print("Congratulations, You got it right. You must be cheating?")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("Damn, you really suck at this.")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))

    print("==============================")
    print("Next Question")
    print("==============================")
    Q4 = input("This Marvel character is from the planet Titan and they killed their whole family. Was it a) Green Goblin, b) Loki, c) Thanos, or d) Nick Fury ")
        
    if Q4 == "c":
        print("==============================")
        print("How did you even know that? You are doing great!")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("Wow, you really got that one wrong?")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))
        
    print("==============================")
    print("Next Question")
    print("==============================")
    Q5 = input("What Marvel character is a master strategist and problem solver who is an expert in close-quarter combat, various human and alien firearms, and battle techniques? Is it a) Groot, b) Star Lord, c) Doctor Strange, or d) Captain Marvel ")
        
    if Q5 == "b":
        print("==============================")
        print("Great Work, You are amazing!")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
        winLose.avengerStatus()
    else:
        print("==============================")
        print("We are just going to ignore that you got that wrong")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))
        winLose.avengerStatus()

