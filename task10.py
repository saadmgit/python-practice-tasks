
# TASK 10: 1 parent class and 2 child classes

class Person:                               # Parent Class

    def getGender(self):
        print("Person class")


class Male(Person):                         # Child Class : Male
    def getGender(self):
        print("Male")


class Female(Person):                       # Child Class : Female
    def getGender(self):
        print("Female")


if __name__ == "__main__":

    person = Person()
    person.getGender()

    male = Male()
    male.getGender()

    female = Female()
    female.getGender()

