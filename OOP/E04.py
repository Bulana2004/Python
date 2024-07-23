class Student(object):
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
        self.age = None
        self.marks = None

    def display(self):
        print(f"Name is : {self.name}")
        print(f"Student id is {self.studentId}")
        print(f"Age is : {self.age}")
        print(f"Marks are {self.marks}")

    def setAge(self, age):
        self.age = age
    
    def setMarks(self, marks):
        self.marks = marks
    
Student = Student("Bulana" , "1234")
Student.setAge(20)
Student.setMarks(50)
Student.display()