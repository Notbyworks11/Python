class Point:
    def __init__(self, x ,y ):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
p1= Point(4,5)
p1._x=6
print(p1.x)