
# TASK 6: code for finding digits and alphabets in a given string

alphabets = 0
digits = 0
input_str = input("please input a string : ")      # user-input string

for i in input_str:                 # loop to traverse on given string
    if i.isdigit():                 # checking each index of string if it is digit or not
        digits += 1                 # incrementing "digit" variable that will store the count of digits

    elif i.isalpha():               # checking each index of string if it is alphabet or not
        alphabets += 1              # incrementing "alphabets" variable that will store the count of alphabets


print("LETTERS :", alphabets)       # final count of alphabets are stored in variable "alphabets"
print("DIGITS :", digits)           # final count of alphabets are stored in variable "alphabets"
