#Create a note-taking program:

import os.path as osp
prompt = "This file already exists.\n\n"
prompt += "If you would like to read the contents enter: r\n"
prompt += "If you would like overwrite please enter: w\n"
prompt += "If you would like to add text please enter: a\n"
file_name = input('Please enter a file name: ')
if osp.isfile(file_name):
    users_choice = input(prompt)
    users_file = open(file_name, user_choice)
    if users_choice == "w" or users_choice == "a":
        users_file.write(input("Enter your text: ") + "\n")
        users_file.close()
    elif users_choice == "r":
        users_file = open(file_name, 'r')
        for line in users_file:
            print(line)
        users_file.close()
else:
    users_file = open(file_name, 'w')
    users_file.write(input('Enter your text: '))
    users_file.close()
users_file.close()