#Problem 2 Solution

#init company list
Company = []

#define Human object
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #added self to company
    def creation(self):
        Company.append(self)

#adding hard coded workers
worker = Human("Bob", 25)
worker.creation()
worker = Human("Alice", 20)
worker.creation()
worker = Human("Carol", 30)
worker.creation()
worker = Human("Dave", 35)
worker.creation()

#calculations
def Calculate():
    AvgAge = 0
    Oldest = ""
    Youngest = ""

    for item in Company:
        AvgAge = AvgAge + item.age

    for item in Company:
        if Oldest == "":
            Oldest = item
        else:
            if item.age > Oldest.age:
                Oldest = item

    for item in Company:
        print(item.name)
        if Youngest == "":
            Youngest = item
        else:
            if item.age < Youngest.age:
                Youngest = item

    AvgAge = AvgAge / len(Company)
    print("Youngest: " + str(Youngest.age))
    print("Average: " + str(AvgAge))
    print("Oldest: " + str(Oldest.age))
    interface()


def interface():
    print("Welcome to the company database.")
    print("What would you like to do? (enter corresponding number)")
    print("1. list all current members")
    print("2. add a member")
    print("3. remove a member")
    answer = input()
    if answer == "1":
        Calculate()
    if answer == "2":
        addMember()
    if answer == "3":
        removeMember()

def addMember():
    print("You have chosen to add a member")
    Name = input("Please enter the Employees Name\n")
    Age = int(input("Please enter the employees age\n"))
    print("Adding to employee directory...")
    worker = Human(Name, Age)
    Company.append(worker)
    print("Employee added!")
    interface()

def removeMember():
    print("You have chosen to remove a member")
    Name = input("Please enter the name of the person you want to fire:\n")
    for item in Company:
        if item.name == Name:
            Company.remove(item)
    interface()



interface()