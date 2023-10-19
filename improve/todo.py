# This for a todo list. Develop an application that allows users to add, remove, and update tasks in a to-do list.

key = input("Please enter your Username: ")
value = input("Please enter your Passsword: ")

my_dict = {key: value}


def create_user(my_dict):
    file_one = open("improve/credentials.txt", "a")
    file_one.write(str(my_dict))
    file_one.close()

def view_user(my_dict):
    file_one = open("improve/credentials.txt", "r")
    my_dict = eval(file_one.read())
    value = my_dict.get(key)
    print(value)
    file_one.close()

create_user(my_dict)
"""
def edit_todo(my_dict):
    file_one = open("improve/credentials.txt", "a")
    file_one.write(my_dict)
    file_one.close()

def remove_todo(my_dict):
    file_one = open("improve/credentials.txt", "a")
    file_one.write(my_dict)
    file_one.close()
"""