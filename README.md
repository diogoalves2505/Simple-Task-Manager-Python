# Simple-Task-Manager-Python
A very simple task manager in python (great for begginers)


This is a simple to-do list program that allows the user to add, remove, and display tasks. Additionally, the program tracks the user's level based on the number of tasks they remove from the list.

The program reads the user's name from a file called "username.txt" and the user's level from a file called "level.txt". If these files do not exist, the program prompts the user to provide a username and creates a "level.txt" file with the initial level set to 1 and XP set to 0.

Every time a task is removed from the list, the program adds 10 XP points to the user. If the total XP is greater than or equal to 100, the program increases the user's level by 1 and decreases the XP by 100.

The program allows the user to change their username and exit the program.
