from gameComponents import gameVars, winLose

def game():
    gameVars.avengerPoints = 0
    print("Here is your first question")
    print("==============================")
    Q1 = input("What Superhero was created as a super soldier to fight in WW2? Was it a) Iron Man, b) Captain America, c) The Hulk, or d) Black Widow ")

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
    Q5 = input("In the first Spiderman movie, Peters best friend was Harry Osborne. Which Villan was Harry's Father? Was it a) SandMan, b) Dr. Otto Octavious, c) Green Goblin, or d) Venom ")
        
    if Q5 == "c":
        print("==============================")
        print("Excellent Work!")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("You suck")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))

    print("==============================")
    print("Next Question")
    print("==============================")
    Q6 = input("What Marvel character does not age and wears an eyepatch? Is it a) Jack Sparrow, b) Nick Fury, c) Bruce Banner, or d) Hawkeye ")
        
    if Q6 == "b":
        print("==============================")
        print("Why didn't you guess Jack Sparrow? Just kidding, great work!")
        gameVars.avengerPoints = gameVars.avengerPoints + 1
        print("Avenger Points: " + str(gameVars.avengerPoints))
    else:
        print("==============================")
        print("Good try, NOT.")
        print("No Avenger points for you, Dirtbag")
        print("Avenger Points: " + str(gameVars.avengerPoints))

    print("==============================")
    print("Next Question")
    print("==============================")
    Q7 = input("What Marvel characters real name is James Howlett and first appeared in an issue of the Incredible Hulk Comic Book? Is it a) Wolverine, b) Spiderman, c) Deadpool, or d) Black Panther ")
        
    if Q7 == "a":
        print("==============================")
        print("Damn, you must have read the comic to know that, or you are just a huge Marvel fan")
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
    Q8 = input("What Marvel character is a master strategist and problem solver who is an expert in close-quarter combat, various human and alien firearms, and battle techniques? Is it a) Groot, b) Star Lord, c) Doctor Strange, or d) Captain Marvel ")
        
    if Q8 == "b":
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

