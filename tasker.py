import cursor

cursor.hide()
import os
import time
import random
import json
from colorama import Fore, Back, Style

os.system("title " + "Tasker")


# Sleep function
def sleep(x):
    time.sleep(x)


# Initialize an empty task dictionary
tasks = {}


def rs():
    return Style.RESET_ALL


# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}


# Load tasks when the program starts
load_tasks()


# Function to add a task
def add_task(task_name, task_description):
    cursor.hide()
    os.system("cls")
    tasks[task_name] = task_description
    save_tasks()
    print(Style.BRIGHT + Fore.GREEN + f"Task '{task_name}' added")
    sleep(2)
    os.system("cls")


# Function to delete a task
def delete_task(task_name):
    cursor.hide()
    os.system("cls")
    if task_name in tasks:
        del tasks[task_name]
        save_tasks()
        print(Style.BRIGHT + Fore.RED + f"Task '{task_name}' deleted")
    else:
        print(Style.BRIGHT + Fore.RED + f"Task '{task_name}' not found")
    sleep(2)
    os.system("cls")


# Function to list all tasks
def list_tasks():
    cursor.hide()
    os.system("cls")
    if tasks:
        for task_name, task_description in tasks.items():
            print(f"{Style.NORMAL + task_name}: {Style.DIM + task_description}" + rs())
        input(Style.DIM + "\nPress enter to return..." + rs())
        os.system("cls")
    else:
        print(Style.BRIGHT + Fore.RED + "Task list is empty." + rs())
        sleep(2)
        os.system("cls")


def rename_task(old_name, new_name):
    cursor.hide()
    if old_name in tasks:
        tasks[new_name] = tasks.pop(old_name)
        save_tasks()
        print(Style.BRIGHT + Fore.GREEN + f"Task '{old_name}' renamed to '{new_name}'.")
    else:
        print(Style.BRIGHT + Fore.RED + f"Task '{old_name}' not found.")


def greet_user():
    current_time = time.localtime().tm_hour
    if 5 <= current_time < 12:
        print(Style.BRIGHT + Fore.YELLOW + "Good morning!\n" + rs())
        sleep(1.8)
        os.system("cls")
    elif 12 <= current_time < 17:
        print(Style.BRIGHT + Fore.YELLOW + "Good afternoon\n" + rs())
        sleep(1.8)
        os.system("cls")
    else:
        print(Style.BRIGHT + Fore.YELLOW + "Good evening\n" + rs())
        sleep(1.8)
        os.system("cls")


greet_user()
# Main loop
while True:
    print(Style.BRIGHT + Fore.YELLOW + "What would you like to do?\n" + rs())
    print(Style.DIM + "1 " + Style.NORMAL + Fore.GREEN + "Add" + rs())
    print(Style.DIM + "2 " + Style.NORMAL + Fore.RED + "Delete" + rs())
    print(Style.DIM + "3 " + Style.NORMAL + Fore.MAGENTA + "List" + rs())
    print(Style.DIM + "4 " + Style.NORMAL + Fore.CYAN + "Rename" + rs())

    cursor.show()
    choice = input(Style.DIM + "\n$ " + rs())

    if choice == "1":
        os.system("cls")
        task_name = input(Style.BRIGHT + Fore.GREEN + "Task name: " + rs())
        os.system("cls")
        task_description = input(
            Style.BRIGHT + Fore.GREEN + f"Task description ({task_name}): " + rs()
        )
        os.system("cls")
        add_task(task_name, task_description)
    elif choice == "2":
        os.system("cls")
        task_name = input(Style.BRIGHT + Fore.RED + "Task name: " + rs())
        delete_task(task_name)
    elif choice == "3":
        list_tasks()
    elif choice == "4":
        os.system("cls")
        old_name = input(Style.BRIGHT + Fore.CYAN + "Task name: " + rs())
        os.system("cls")
        new_name = input(Style.BRIGHT + Fore.CYAN + "New task name: " + rs())
        os.system("cls")
        rename_task(old_name, new_name)
        sleep(2)
        os.system("cls")
    elif choice == "help":
        cursor.hide()
        os.system("cls")
        print(Style.BRIGHT + Fore.YELLOW + "Tasker v0.1\n" + rs())
        print("Commands:")
        print(f"Type '1' to {Fore.GREEN + 'add' + rs()} a task" + rs())
        print(f"Type '2' to {Fore.RED + 'delete' + rs()} a task" + rs())
        print(f"Type '3' to {Fore.MAGENTA + 'list' + rs()} all tasks" + rs())
        print(f"Type '4' to {Fore.CYAN + 'rename' + rs()} a task" + rs())
        print(f"Type 'greet' to {Fore.YELLOW + 'greet' + rs()} the user" + rs())
        print(f"Type 'exit' to {Fore.RED + 'exit' + rs()} the program" + rs())
        input(Style.DIM + "\nPress enter to return..." + rs())
        os.system("cls")
    elif choice == "greet":
        cursor.hide()
        os.system("cls")
        greet_user()
    elif choice == "exit":
        cursor.hide()
        os.system("cls")
        goodbye_messages = [
            "Goodbye!",
            "See you later!",
            "Farewell!",
            "Bye!",
            "Have a nice day!",
        ]
        print(Style.BRIGHT + Fore.YELLOW + random.choice(goodbye_messages) + rs())
        sleep(1.5)
        break
    else:
        cursor.hide()
        os.system("cls")
        print(Style.BRIGHT + Fore.RED + "Invalid choice: " + rs() + choice)
        sleep(2)
        os.system("cls")
