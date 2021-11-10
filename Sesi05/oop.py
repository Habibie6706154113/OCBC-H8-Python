print('helo')

class Dog:
    species = 'Cenis Familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog('Miles', 4)
print(miles.name)
print(miles.age)
print(miles.species)
print(miles.description())
print(miles.speak('bark'))
print()

buddy = Dog('Buddy', 9)
print(buddy.name)
print(buddy.age)
print(buddy.species)
print(buddy.description())
print(buddy.speak('bark'))

class Mom:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

class Children(Mom):
    def __init__(self, name, hair_color, age):
        super().__init__(name, hair_color)
        self.age = age

mom = Mom('ani', 'coklat')
print(f"{mom.name}'s hair color is {mom.hair_color}")
first_doughter = Children('ita', 'ungu', 12)
print(f"{first_doughter.name}'s hair color is {first_doughter.hair_color} and {first_doughter.name} is {first_doughter.age} years old")
print()