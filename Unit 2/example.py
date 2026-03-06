class Student:
    def __init__(self, name, age, grade, GPA):
        self.name = name
        self.age = age
        self.grade = grade
        self.GPA = GPA

    def attendClass(self, name):
        print(self.name + "is attending class.")

    def doHomework(self, name):
        print(self.name + "is doing homework.")

    def study(self, name):
        print(self.name + "has a test tomorrow.")
        print(self.name + "is studying for the test.")

    def study(self, grade):
        print(self.name + " is studying for " + grade)


    s1 = Student("Harry", "17", "12th", "4.0")
    s2 = Student("Roy", "17", "12th", "4.5")