
# TASK 4: code for making input string UPPERCSASE using class & methods

class SaadCls:

    def __init__(self):                     # init function initializing input string variable
        self.input_str = ""

    def get_string(self):                   # Method for taking input from user
        self.input_str = input("please enter string : ")        # user-input string and declaring it to variable

    def print_string(self):                 # Method for displaying uppercase string
        print("Upper case string is : " + self.input_str.upper())     # Using Built-in function to make string in UPPER CASE


if __name__ == "__main__":

    obj1 = SaadCls()                    # Class object initializing
    obj1.get_string()                   # Method calling 1
    obj1.print_string()                 # Method calling 2


