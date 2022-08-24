import random
user = "Y"
print("Welcome to New Stone Paper Scissors Game")
while(user == "Y"):
    choice = input("Press S for Stone \nPress P for Paper \nPress T for Scissors\n: ").upper()
    if choice != "S" and choice != "P" and choice != "T":
        print("Invalid Input")
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
            
    print("Computer selected - ", cpu_select(cpu_choice))

    if (choice == "P" and cpu_choice == "S") or (choice == "T" and cpu_choice == "P") or (choice == "S" and cpu_choice == "T"):
        print("You Win, Congratulations!")
    elif (choice == "S" and cpu_choice == "P") or (choice == "P" and cpu_choice == "T") or (choice == "T" and cpu_choice == "S"):
        print("You Lose, Better luck next time!")
    else:
        print("It's a draw")

    user = input("Play Again? Y for yes N for No: ").upper()
