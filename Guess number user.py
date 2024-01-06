#computer guess number
import random
def computer_guess(x):
    low=1
    high=x
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too High (H),too low (L) or Correct (C): ").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f"Yay !. computer guess the number {guess} Correctly!!")

computer_guess(1)            

#yahan jo guess variable hai wo loop ka andr likha hai lakin wo bahir bhi access ho rah hai q ka wo function ka scope main age hum aik function
#bnae aur us main loop lgain aur us looop main aik variable bnae us variable hum function ka andr aur loop sa bahir access kar skta hai  














