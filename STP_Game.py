import random
user = "Y"
print("Welcome to Stone Paper Scissors")
while(user == "Y"):
    choice = input("Enter your choice S for Stone P for Paper and T for Scissors: ").upper()
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
            
    print("CPU selected", cpu_select(cpu_choice))

    if (choice == "P" and cpu_choice == "S") or (choice == "T" and cpu_choice == "P") or (choice == "S" and cpu_choice == "T"):
        print("You Win")
    elif (choice == "S" and cpu_choice == "P") or (choice == "P" and cpu_choice == "T") or (choice == "T" and cpu_choice == "S"):
        print("You Lose")
    else:
        print("No one Wins")

    user = input("Play Again? Y for yes N for No: ").upper()
