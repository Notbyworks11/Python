class Car():
    def __init__(self,color, mileage):
        self.color = color 
        self.mileage = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage:,} miles."
    

Blue = Car("Blue", 20000)
Red = Car ("Red", 30000)
print(Blue.description())
print(Red.description())
