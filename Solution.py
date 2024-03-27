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

print(len(Company))

#calculations
def Calculate(Company):
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
        if Youngest == "":
            Youngest = item
        else:
            if item.age < Youngest.age:
                Youngest = item

    AvgAge = AvgAge / len(Company)
    print("Youngest: " + str(Youngest.age))
    print("Average: " + str(AvgAge))
    print("Oldest: " + str(Oldest.age))
    
Calculate(Company)


def interface():
    print("Welcome to the company database.")
    