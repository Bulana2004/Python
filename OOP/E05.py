class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def ChechAngle(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)
print(f"{my_triangle.number_of_sides}")
print(f"{my_triangle.ChechAngle()}")
