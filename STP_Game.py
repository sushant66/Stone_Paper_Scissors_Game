import random
user = "Y"
print("Welcome to Stone Paper Scissors\n")
print("Please Enter your Name : ")
name = input()
print("Let's start Stone Paper Scissors")
while(user == "Y"):
    try:
        choice = map(str,input("Enter \"S\" - Stone, \"P\" - Paper, \"T\" - Scissors: ").upper())
        #print(choice)
        if choice[0] != "S" and choice[0] != "P" and choice[0] != "T":
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
                
        print("CPU selected", cpu_select(cpu_choice))

        if (choice == "P" and cpu_choice == "S") or (choice == "T" and cpu_choice == "P") or (choice == "S" and cpu_choice == "T"):
            print(str(name) + " Won")
        elif (choice == "S" and cpu_choice == "P") or (choice == "P" and cpu_choice == "T") or (choice == "T" and cpu_choice == "S"):
            print("Computer Won")
        else:
            print("Its a draw")

        user = input("Play Again? \"Y\" - yes \"N\" - No : ").upper()
    except:
        user = "Y"
        print("Please enter valid input")

