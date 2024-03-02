import random
while True:
    user_input = input("Press 'y' to START the Game OR 'q' to QUIT:\n")
    if user_input.lower() == "q":
        print("-----GAME OVER-----")
        print("Thanks for Playing!")
        break
    elif user_input.lower() == "y":
        while True:
            random_number = random.randint(1, 6)
            if random_number == 1:
                print("[-----]")
                print("[  0  ]")
                print("[-----]")
            if random_number == 2:
                print("[-------]")
                print("[ 0     ]")
                print("[     0 ]")
                print("[-------]")
            if random_number == 3:
                print("[-------]")
                print("[ 0     ]")
                print("[   0   ]")
                print("[     0 ]")
                print("[-------]")
            if random_number == 4:
                print("[-------]")
                print("[ 0   0 ]")
                print("[ 0   0 ]")
                print("[-------]")
            if random_number == 5:
                print("[-------]")
                print("[ 0   0 ]")
                print("[   0   ]")
                print("[ 0   0 ]")
                print("[-------]")
            if random_number == 6:
                print("[-------]")
                print("[ 0    0]")
                print("[ 0    0]")
                print("[ 0    0]")
                print("[-------]")
            user_input = input("Press 'y' to Roll Again OR 'q' to QUIT:\n")
            if user_input.lower() == "q":
                print("-----GAME OVER-----")
                print("Thanks for Playing!")
                break
    else:
        print("Invalid input. Please enter 'y' to START OR 'q' to QUIT:\n")
