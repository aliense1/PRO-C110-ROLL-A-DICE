import random

agree = input("press y to roll the dice and n to exit:")

while agree == "y":

    no = random.randint(1,6)

    if no ==1:
       print("[-------]")
       print("[       ]")
       print("[   0   ]")
       print("[       ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")

    if no ==2:
       print("[-------]")
       print("[       ]")
       print("[  0  0 ]")
       print("[       ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")

    if no ==3:
       print("[-------]")
       print("[       ]")
       print("[0  0  0]")
       print("[       ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")

    if no ==4:
       print("[-------]")
       print("[ 0   0 ]")
       print("[       ]")
       print("[ 0   0 ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")

    if no ==5:
       print("[-------]")
       print("[ 0   0 ]")
       print("[   0   ]")
       print("[ 0   0 ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")

    if no ==6:
       print("[-------]")
       print("[ 0 0 0 ]")
       print("[       ]")
       print("[ 0 0 0 ]")
       print("[-------]")
       agree = ""
       agree = input("press y to roll the dice and n to exit:")
    

    if agree == "n":
       print("Thanks for playing")
       break
       
        