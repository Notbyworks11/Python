class Animal():
    species = "Mammal"
    def __init__(self, name,sound):
        self.name = name
        self.sound = sound 

    def speak(self):
        return f"{self.name} says {self.sound}"
    
#instantiation (a new instance  is located at a different memory address)
Animal1 = Animal("Dog" , "Woof")
Animal1.name = "Cat"
Animal1.sound = "Meow"

print(Animal1.speak())