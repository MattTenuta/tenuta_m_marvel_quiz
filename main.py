from gameComponents import playingGame

print("==============================")
print("Welcome to my Marvel character quiz made using python")
print("==============================")
print("Follow these simple rules if you want to survive")
print("You will be asked a question about a Marvel character and you must provide the correct answer")
print("For each correct answer you will earn 1 Avenger Point")
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
        playingGame.game()
      
