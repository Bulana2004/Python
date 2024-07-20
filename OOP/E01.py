class circle (object):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius * self.radius

    def circumFerence(self):
        return 2 * 3.14 * self.radius


x = int(input("Enter area to calculate : "))
circle = circle(x)

print(f"Area {circle.getArea()}")
print(f"CicircumFerence {circle.circumFerence()}")
