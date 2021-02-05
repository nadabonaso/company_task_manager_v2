# This is a Task Manager application which is designed to help team members manage tasks which are assigned to them.

# Import statements
import os
from datetime import date
from datetime import datetime


# Global variables set here.
today = date.today()
logged_in = False
num_tasks = 0
num_users = 0
num_overdue = 0
num_incomplete_overdue = 0


# Defines function to check user and password.
def get_user(user, password):
    return user, password


# Adds menu list.
def menu(reg_user, add_task, tasks, my_task, stats, reports, exit):
    menu_list = [reg_user, add_task, tasks, my_task, stats, reports, exit]
    return menu_list


# Prints menu list depending on the user, it will display different menu items.
def print_menu():
    titles = ["r\t-\tRegister a user", "a\t-\tAdd a task", "va\t-\tView all tasks", "vm\t-\tView my tasks",
              "vs\t-\tView statistics", "gr\t-\tGenerate reports", "e\t-\tExit program"]

    for i in range(len(titles)):
        if user == "admin" and password == "adm1n":
            print(titles[i])

    if user != "admin" and password != "adm1n":
        unwanted = [0, 4, 5]

        for i in sorted(unwanted, reverse=True):
            del titles[i]
        titles_str = "\n".join(titles)
        print(titles_str)


# Writes user and password to file when adding a new user.
def write_user_to_file(user, password):
    user_file = open("user.txt", "a+")
    user_file.write(f"\n{user}, {password}")
    user_file.close()


# Add new user list.
def user_list(user, password, password_check):
    add_user_list = [user, password, password_check]
    return add_user_list


# Function to register a new user.
def reg_user_check(user, password, password_check):
    while True:
        user_file = open("user.txt", "r")
        user_file_read = user_file.readlines()

        # Checks if the username exists in the user text file.
        for line in user_file_read:
            if user in line:
                print("\nUsername exists, try again.\n")
                user = input("Enter username\t: ")
                password = input("Enter password\t: ")
                password_check = input("Re-enter password\t: ")

        # Checks if the passwords do not match.
        if password != password_check:
            print("\nPasswords do not match, please try again.\n")
            user = input("Enter username\t: ")
            password = input("Enter password\t: ")
            password_check = input("Re-enter password\t: ")

        # Checks if the passwords match.
        elif password == password_check:
            # Calls the function to write new user and password to file.
            write_user_to_file(user, password)
            print("\nYou have successfully added a new user.\n")
            break

        user_file.close()


# Adds new task and makes it a list.
def add_task(user, id_num, title, assigned_date, due_date, is_completed, descrip):
    user_task_list = [user, id_num, title, assigned_date, due_date, is_completed, descrip]
    return user_task_list


# Allows user to add the new task in interface.
def task_data(list_a):
    titles = ["Assigned to", "Task ID", "Task title", "Date created", "Due date", "Completed?", "Description"]

    for i in range(len(titles)):
        print("{:<12} {:<2} {:<2}".format(titles[i], ":", list_a[i]))

    print("----------------------------------------")


# Writes the new task to a text file.
def write_task(list_a):
    task_file = open("tasks.txt", "a")

    # Iterate over each line in tasks text file.
    for i in range(0, len(list_a)-1):
        task = list_a[i] + "$"
        task_file.write(task)

    task_file.write(list_a[-1])
    task_file.write("\n")
    task_file.close()


# Displays all the tasks back to the user.
def view_all():
    task_file = open("tasks.txt", "r")
    found_task = False

    # Iterate over each line in file.
    for line in task_file:
        line = line.rstrip("\n")
        user, id_num, title, descrip, assigned_date, due_date, is_completed = line.split("$")

        # check if size of file is not 0
        if os.stat("tasks.txt").st_size != 0:
            found_task = True
            task_data(add_task(user, id_num, title, assigned_date, due_date, is_completed, descrip))

    # If no tasks, display message.
    if found_task == False:
        print("\nThere are currently no tasks.\n")
    task_file.close()


# Displays only the logged in user's tasks.
def view_mine():
    task_file = open("tasks.txt", "r")
    found_task = False

    # Iterate over each line in file.
    for line in task_file:
        line = line.rstrip("\n")
        user, id_num, title, descrip, assigned_date, due_date, is_completed = line.split("$")

        # Checks if logged in user has tasks.
        if user == detect_user_tasks:
            if is_completed == "No":
                found_task = True
                task_data(add_task(user, id_num, title, assigned_date, due_date, is_completed, descrip))

    # If no tasks, display message.
    if found_task == False:
        print("\nYou have no tasks!\n")

    task_file.close()


# Calculates and returns the total number of tasks.
def get_total_tasks(num_tasks):
    task_file = open("tasks.txt", "r")
    content = task_file.read()
    task_list = content.split("\n")

    # Iterate over each line in tasks text file.
    for i in task_list:
        if i:
            num_tasks += 1

    task_file.close()
    return num_tasks


# Calculates and returns the total number of completed tasks.
def get_num_complete_tasks(user):
    t = 0
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()
    str_comp = "Yes"

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")
        # Checks the 'is completed' data in list.
        if str_comp in i[6]:
            if user in i[0]:
                t += 1

    task_file.close()
    return t


# Calculates and returns the total number of uncompleted tasks.
def get_total_num_complete_tasks(t):
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")

        # Checks the 'is completed' data in list.
        if i[6] == "Yes\n":
            t += 1

    task_file.close()
    return t


# Calculates and returns the total number of uncompleted tasks.
def get_num_incomplete_tasks(t):
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")

        # Checks the 'is completed' data in list.
        if i[6] == "No\n":
            t += 1

    task_file.close()
    return t


# Calculates and returns the total number of overdue tasks.
def get_num_overdue_tasks(num_is_overdue):
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")
        # Checks the due date and compares with the current date.
        due_date_str = i[4]
        due_date_object = datetime.strptime(due_date_str, '%Y-%m-%d').date()

        # If overdue, add counter.
        if due_date_object <= today:
            num_is_overdue += 1

    task_file.close()
    return num_is_overdue


# Function to calculate and return the total number of overdue and uncompleted tasks.
def get_num_incomplete_overdue(num_incomplete_overdue):
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")
        due_date_str = i[4]
        due_date_object = datetime.strptime(due_date_str, '%Y-%m-%d').date()

        if due_date_object <= today and i[6] == "No\n":
            num_incomplete_overdue += 1

    task_file.close()
    return num_incomplete_overdue


# Function to calculate and return the total number of overdue and uncompleted tasks.
def get_num_incomplete_overdue_user(user):
    task_file = open("tasks.txt", "r")
    content = task_file.readlines()
    t = 0

    # Iterate over each line in tasks text file.
    for i in content:
        i = i.split("$")
        # If username matched the first index, checks if the due date has expired.
        if user == i[0]:
            due_date_str = i[4]
            due_date_object = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            # If due date is in the future and task is marked 'not complete' then adds 1.
            if due_date_object <= today and i[6] == "No\n":
                t += 1

    task_file.close()
    return t


# Generates report for task overview.
def gen_report_tasks():
    total = get_total_tasks(num_tasks)
    complete = get_total_num_complete_tasks(num_tasks)
    incomplete = total - complete
    incomplete_tasks_percent = incomplete / total
    overdue = get_num_overdue_tasks(num_overdue)
    overdue_tasks = overdue / total
    incomplete_overdue = get_num_incomplete_overdue(num_incomplete_overdue)
    # Writes task overview to text file.
    task_overview = open("task_overview.txt", "w")
    task_overview.write("TASK OVERVIEW REPORT\n----------------------------------------\n")
    task_overview.write("{:<25} {:<4} {:<2}\n".format("Total number of tasks", ":", total))
    task_overview.write("{:<25} {:<4} {:<2}\n".format("Total completed tasks", ":", complete))
    task_overview.write("{:<25} {:<4} {:<2}\n".format("Total uncompleted tasks", ":", incomplete))
    task_overview.write("{:<25} {:<4} {:<2}\n".format("Uncompleted and overdue", ":", incomplete_overdue))
    task_overview.write("{:<25} {:<4} {:<2.0%}\n".format("Percentage uncompleted", ":", incomplete_tasks_percent))
    task_overview.write("{:<25} {:<4} {:<2.0%}\n".format("Percentage overdue", ":", overdue_tasks))
    task_overview.close()


# Gets the same data in task overview report and displays to user.
def display_report_tasks():
    total = get_total_tasks(num_tasks)
    complete = get_total_num_complete_tasks(num_tasks)
    incomplete = total - complete
    incomplete_tasks_percent = incomplete / total
    overdue = get_num_overdue_tasks(num_overdue)
    overdue_tasks = overdue / total
    incomplete_overdue = get_num_incomplete_overdue(num_incomplete_overdue)
    print("\nTASK STATISTICS\n----------------------------------------")
    print("{:<25} {:<4} {:<2}".format("Total number of tasks", ":", total))
    print("{:<25} {:<4} {:<2}".format("Total completed tasks", ":", complete))
    print("{:<25} {:<4} {:<2}".format("Total uncompleted tasks", ":", incomplete))
    print("{:<25} {:<4} {:<2}".format("Uncompleted and overdue", ":", incomplete_overdue))
    print("{:<25} {:<4} {:<2.0%}".format("Percentage uncompleted", ":", incomplete_tasks_percent))
    print("{:<25} {:<4} {:<2.0%}".format("Percentage overdue", ":", overdue_tasks))


# Calculates and returns the total number of users.
def get_total_users(num_users):
    user_file = open("user.txt", "r")
    content = user_file.read()
    user_list = content.split("\n")

    # Iterate over each line in user text file.
    for i in user_list:
        if i:
            num_users += 1

    user_file.close()
    return num_users


# Generates report for user overview.
def gen_report_users():
    total_users = get_total_users(num_users)
    total_tasks = get_total_tasks(num_tasks)
    # Writes user overview to text file.
    user_overview = open("user_overview.txt", "w")
    user_overview.write("USER OVERVIEW REPORT\n----------------------------------------\n")
    user_overview.write("{:<28} {:<4} {:<2}\n".format("Total number of users", ":", total_users))
    user_overview.write("{:<28} {:<4} {:<2}\n".format("Total number of tasks", ":", total_tasks))
    task_file = open("tasks.txt", "r")
    # Create an empty dictionary.
    task_dict = dict()

    # Loop through each line of the file of task text file.
    for line in task_file:
        line = line.split("$")
        user = line[0]

        # Check if the user is already in dictionary.
        if user in task_dict:
            # Increment count of user by 1.
            task_dict[user] = task_dict[user] + 1
        else:
            # Add the user to dictionary with count 1.
            task_dict[user] = 1

    # Writes the contents of dictionary to text file.
    for key in list(task_dict.keys()):
        num_user_tasks = task_dict[key]
        total = get_total_tasks(num_tasks)
        perc_total = num_user_tasks / total
        num_complete = get_num_complete_tasks(key)
        perc_complete = num_complete / num_user_tasks
        num_incomplete = num_user_tasks - num_complete
        perc_uncomplete = num_incomplete / num_user_tasks
        incomplete_overdue = get_num_incomplete_overdue_user(key)
        perc_uncomplete_overdue = incomplete_overdue / num_user_tasks
        user_overview.write("----------------------------------------\n")
        user_overview.write("{:<28} {:<4} {:<2}\n".format("Username", ":", key))
        user_overview.write("{:<28} {:<4} {:<2}\n".format("Total tasks for user", ":", task_dict[key]))
        user_overview.write("{:<28} {:<4} {:<2.0%}\n".format("Percentage of all tasks", ":", perc_total))
        user_overview.write("{:<28} {:<4} {:<2.0%}\n".format("Percentage completed", ":", perc_complete))
        user_overview.write("{:<28} {:<4} {:<2.0%}\n".format("Percentage uncompleted", ":", perc_uncomplete))
        user_overview.write("{:<28} {:<4} {:<2.0%}\n".format("% Uncompleted and overdue", ":", perc_uncomplete_overdue))

    user_overview.close()
    task_file.close()


# Gets the same data as user overview report and displays to user.
def display_report_users():
    total_users = get_total_users(num_users)
    total_tasks = get_total_tasks(num_tasks)
    # Prints the total users and total tasks on screen for user.
    print("\nUSER STATISTICS\n----------------------------------------")
    print("{:<28} {:<4} {:<2}".format("Total number of users", ":", total_users))
    print("{:<28} {:<4} {:<2}".format("Total number of tasks", ":", total_tasks))
    task_file = open("tasks.txt", "r")
    # Create an empty dictionary.
    task_dict = dict()

    # Loop through each line of the file of task text file.
    for line in task_file:
        line = line.split("$")
        user = line[0]

        # Check if the user is already in dictionary.
        if user in task_dict:
            # Increment count of user by 1.
            task_dict[user] = task_dict[user] + 1
        else:
            # Add the user to dictionary with count 1.
            task_dict[user] = 1

    # Prints the contents of dictionary on screen for user.
    for key in list(task_dict.keys()):
        num_user_tasks = task_dict[key]
        total = get_total_tasks(num_tasks)
        perc_total = num_user_tasks / total
        num_complete = get_num_complete_tasks(key)
        perc_complete = num_complete / num_user_tasks
        num_incomplete = num_user_tasks - num_complete
        perc_uncomplete = num_incomplete / num_user_tasks
        incomplete_overdue = get_num_incomplete_overdue_user(key)
        perc_uncomplete_overdue = incomplete_overdue / num_user_tasks
        print("----------------------------------------")
        print("{:<28} {:<4} {:<2}".format("Username", ":", key))
        print("{:<28} {:<4} {:<2}".format("Total tasks for user", ":", num_user_tasks))
        print("{:<28} {:<4} {:<2.0%}".format("Percentage of all tasks", ":", perc_total))
        print("{:<28} {:<4} {:<2.0%}".format("Percentage completed", ":", perc_complete))
        print("{:<28} {:<4} {:<2.0%}".format("Percentage uncompleted", ":", perc_uncomplete))
        print("{:<28} {:<4} {:<2.0%}".format("% Uncompleted and overdue", ":", perc_uncomplete_overdue))

    task_file.close()


# This checks the number of tasks in external text file to make a counter for task ID.
with open('tasks.txt') as f:
    tasks = f.readlines()
    size = len(tasks)
    task_id_count = size + 1

# User login displays username and password input.
print("TASK MANAGER LOGIN\n----------------------------------------")
while logged_in == False:
    user = input("Enter username\t:\t").strip()
    password = input("Enter password\t:\t").strip()

    for line in open("user.txt", "r").readlines():
        login_info = line.strip().split(", ")

        if user == login_info[0] and password == login_info[1]:
            logged_in = True
            detect_user_tasks = login_info[0]
            logged_in_user = login_info[0] + ", " + login_info[1]

    if logged_in == False:
        print("\nInvalid entry, please try again.\n")

selection = ""
# Once logged in this displays the option depending on the user's input from menu.
while selection != "e":
    print("\nTASK MANAGER MENU\n----------------------------------------")
    # Calls function to print main menu.
    print_menu()
    selection = input("----------------------------------------\nEnter your selection\t:\t")

    if selection == "r":
        print("\nREGISTER A NEW USER\n----------------------------------------")
        new_user = input("Enter username\t:\t")
        new_password = input("Enter password\t:\t")
        do_password_check = input("Re-enter password\t:\t")
        reg_user_check(new_user, new_password, do_password_check)

    elif selection == "a":
        print("\nADD NEW TASK\n----------------------------------------")
        task_id = str(task_id_count)
        task_id_count += 1
        task_user = input("Who is this task for\t:\t")
        task_title = input("Give the task a title\t:\t")
        task_assigned_date = str(today)
        task_due_date = input("Due date (yyyy-mm-dd)\t:\t")
        task_complete = "No"
        task_descrip = input("Enter task description\t:\t")
        # Calls the add task function.
        task_list = add_task(task_user, task_id, task_title, task_assigned_date, task_due_date, task_complete,
                             task_descrip)
        # Writes the task to file.
        save_task = (task_user, task_id, task_title, task_descrip, task_assigned_date, task_due_date, task_complete)
        write_task(save_task)
        print("\nYour task has been successfully saved.")

    elif selection == "va":
        print("\nALL TASKS\n----------------------------------------")
        # Calls view all tasks function.
        view_all()

    elif selection == "vm":
        print("\nMY TASKS\n----------------------------------------")
        # Calls the function to view only the logged in user's tasks.
        view_mine()
        # Option to edit a task or return to menu.
        edit_id = input("Enter task ID or -1 for main menu\t:\t")
        # Opens tasks.txt to get tasks and add the counter for task IDs.
        task_file = open("tasks.txt", "r+")
        list_of_tasks = task_file.readlines()
        i_count = 0
        s = "$"

        if edit_id != "-1":
            task_file = open("tasks.txt", "w")

            for task in list_of_tasks:
                split_task = task.split("$")

                # Allows user to enter ID to edit the task.
                if edit_id == split_task[1]:
                    print("\nEDIT TASK ID " + split_task[1] + "\n----------------------------------------")
                    # print(task)
                    split_task[6] = input("Is this task complete? (Yes/No)\t:\t")

                    if split_task[6] == "No":
                        edit_task = input("Edit task (Yes/No)\t:\t")

                        if edit_task == "Yes":
                            split_task[0] = input("Who is this task for\t:\t")
                            split_task[5] = input("Due date (yyyy-mm-dd)\t:\t")
                    seq = (
                    str(split_task[0]), str(split_task[1]), str(split_task[2]), str(split_task[3]), str(split_task[4]),
                    str(split_task[5]), str(split_task[6]))
                    task = s.join(seq) + "\n"

                # Writes task to text file.
                task_file.write(task)
                i_count += 1

            print("\nThe task has been updated.\n")
            task_file.close()

    elif selection == "vs":
        # Displays the tasks overview to the user.
        display_report_tasks()
        # Displays the users overview to the user.
        display_report_users()

    elif selection == "gr":
        print("\nGENERATE REPORTS\n----------------------------------------")
        # This generates the Task Overview report.
        gen_report_tasks()
        # This generates the User Overview report.
        gen_report_users()
        print("Your reports have been generated.")

    elif selection == "e":
        # Exits the program.
        print("\nGoodbye!")
        exit(0)

    else:
        print("\nInvalid option.")