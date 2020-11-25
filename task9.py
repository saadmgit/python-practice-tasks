
# TASK 9: user input multiple passwords and validate those passwords
import re                   # Importing modules for use of regular expressions

input_pass = str(input("Enter multiple passwords with comma ',' separated : "))             # Multiple passwords from user input

make_list = input_pass.split(',')                                               # Making input as a List

print("Input LIST : ", make_list)                                               # Original given user LIST

for i in range(len(make_list)):                                             # Validating passwords
    r = re.compile('^(?=\S{6,12}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')       # Password regex for validation
    new_list = list(filter(r.match, make_list))                             # Matching each index according to regex

print("Valid passwords are: ", new_list)                                       # Printing Final LIST of valid passwords
