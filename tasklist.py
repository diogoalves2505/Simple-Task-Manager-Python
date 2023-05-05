import os

# Name of the text file to store user level
filename = "level.txt"

# Read file (username.txt)
with open('username.txt', 'r') as f:
    username = f.read().strip()

# Request new username if file is empty
if not username:
    username = input("Choose your username: ")
    with open('username.txt', 'w') as f:
        f.write(username)


# If file does not exist, create it with initial level 1 and XP 0
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("1\n0")

# Read file contents to get current level and XP
with open(filename, "r") as f:
    level,xp = map(int, f.read().split())

#-----------------------------------------------------------------------------------------

welcome = f"Welcome, {username}!"
print(welcome)

# Open "list.txt" file in read mode, read tasks, and store in list
with open("list.txt", "r") as f:
    list = f.read().splitlines()

#Options menu
print('--------------------------------------')
print("Type '1' to add task.")
print("Type '2' to remove a task.")
print("Type '3' to display tasks.")
print("Type '4' to change username.")
print("Type '5' to quit.")

while True:
    # Get user choice
    print('--------------------------------------')
    choice = input("What would you like to do? ")

    
    if choice == "1":
        # Ask for new task
        task = input("Enter new task: ")

        # Add new task to list and to "lista.txt" file
        list.append(task)
        with open("list.txt", "a") as f:
            f.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":
        # Ask for index of task to be removed
        indice = int(input("Enter the index of the task to be removed: "))

        # Remove task from list and update "lista.txt" file
        list.pop(indice - 1)
        with open("list.txt", "w") as f:
            for task in list:
                f.write(task + "\n")
                xp += 10
                  # If XP is greater than or equal to 100, increase level and decrease XP by 100
                if xp >= 100:
                    level += 1
                    xp -= 100
        print("Congratulations, you leveled up! Your current level is:", level)

        print("Task removed successfully.")


    elif choice == "3":
        # Display tasks enumerated
        for i, task in enumerate(list):
            print(f"{i+1}. {task}")

    elif choice == "4":
        new_name = input('New username: ')
        with open('username.txt','w') as f:
         f.write(new_name)

    elif choice == "5":
        # Quit the program
        print("Exiting the program.")
        break

    else:
        print("Save new level and XP to text file")

 # Save new level and XP to text file
    with open(filename, "w") as f:
        f.write(str(level) + "\n" + str(xp))
