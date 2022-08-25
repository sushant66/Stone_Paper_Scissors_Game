import random
user = "Y"
user_score = 0
computer_score = 0
print("Please Enter your Name below")
name = raw_input()
print("Welcome to Stone Paper Scissors Game, " + str(name))

while(user == "Y"):
    try:
        choice = str(raw_input("Enter \"S\" - Stone, \"P\" - Paper, \"T\" - Scissors: ").upper())
        if(choice[0] != "S" and choice[0] != "P" and choice[0] != "T"):
            print("Game Over, You selection is incorrect!")
            break
        cpu = random.randint(0,2)
        cpu_choice = None
        if cpu == 0:
            cpu_choice = "S"
        elif cpu == 1:
            cpu_choice = "P"
        elif cpu == 2:
            cpu_choice = "T"

        def cpu_select(cpu_choice):
            if cpu_choice == "S":
                return "Stone"
            elif cpu_choice == "P":
                return "Paper"
            elif cpu_choice == "T":
                return "Scissors"
                
        print("Computer selected " + str(cpu_select(cpu_choice)))

        if (choice == "P" and cpu_choice == "S") or (choice == "T" and cpu_choice == "P") or (choice == "S" and cpu_choice == "T"):
            print(str(name) + " Won")
            user_score+=1
            print("Scores : " + name + " = " + str(user_score) + " Computer = " + str(computer_score))
        elif (choice == "S" and cpu_choice == "P") or (choice == "P" and cpu_choice == "T") or (choice == "T" and cpu_choice == "S"):
            print("Computer Won")
            computer_score+=1
            print("Scores : " + name + " = " + str(user_score) + " Computer = " + str(computer_score))
        else:
            print("Its a draw")
            user_score+=1
            computer_score+=1
            print("Scores : " + name + " = " + str(user_score) + " Computer = " + str(computer_score))

        user = raw_input("Play Again? \"Y\" - yes \"N\" - No : ").upper()
        if(user == "N"):
            break
    except:
        user = "Y"
        print("Please enter valid input")

