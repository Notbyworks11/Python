class Circle:
    def __init__(self,radius):
        self.radius = radius
        
        
    @property
    def radius(self):
        return self.radius
    
    
    @radius.setter
    def radius (self, value):
        self.radius = float(value)
        
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2
        
        
    
        