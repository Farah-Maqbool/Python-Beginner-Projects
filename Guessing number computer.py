#Guessing Game
#Through while loop
import random
def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess<random_number:
            print("Try again. [Hint: Too low]")
        elif guess>random_number:
            print("Try again. [Hint:Too High]")  
    print("Congrats. You guess the number")          
guess(10)
#Through for loop
import random
def num(y):
    random_number=random.randint(1,y)
    print("You just five time play this game")
    for i in range(5):
        num=int(input(f"Guess number between 1 and {y}: "))
        if num<random_number:
            print("Try again. [Hint: Too low]")
        elif num>random_number:
            print("Try again. [Hint:Too High]")
        elif num==random_number:
             print("Congrats. You guess the number")    
             break
    else:
        print("Game over")


num(20)                       