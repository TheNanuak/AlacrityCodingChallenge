#Problem 2 Solution
        
Company = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def creation(self):
        Company.append(self)


person = Person("Bob", 25)
person.creation()
person = Person("Alice", 20)
person.creation()
person = Person("Carol", 30)
person.creation()
person = Person("Dave", 35)
person.creation()

for p in Company:
    print(p.name)