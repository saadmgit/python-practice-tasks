
# TASK 8: Take integers input from user as a comma separated

make_list = []
odd_list = []
input_nums = str(input("Enter numbers in comma ',' separated : "))  # Taking input as a comma separated

input_list = input_nums.split(",")                      # Making string a list

for i in input_list:                                    # Making list integer based (it was considered as string when input because comma separated)
    make_list.append(int(i))
print("User input LIST : ", make_list)                                        # final list on which operation is to be done


for num in make_list:                                   # main loop for finding odd nums in list
    if num % 2 != 0:
        odd_list.append(num)                            # making another list of all the odd nums instead of just displaying them

print("ODD numbers LIST : ", odd_list)                                         # List conatining odd numbers
