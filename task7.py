
# TASK 7: taking user input of words in comma separated and make them arrange alphabetically


usr_input = str(input("please insert strings in comma ',' seprated : "))       # Taking user-input in comma separated strings

my_list = usr_input.split(",")                       # Converting input into list for sorting
print("Unsorted list is : ", my_list)                # Printing unsorted list

my_list.sort()                                       # Built-in Function for list sorting

print("Alphabetically sorted list is : ", my_list)   # Sorted list displayed


