x = str("A class property is a varibale that stores data for a class.")
x = str("A class method is an action that a class performs via a function.")

class student:
    def __init__(self, name, age, grade, GPA):
        self.name = name
        self.age = age
        self.grade = grade
        self.GPA = GPA

    def attendClass(name):
        print(self.name + "is attending class.")

    def doHomework(name):
        print(self.name + "is doing homework.")

    def study(name):
        print(self.name + "has a test tomorrow.")
        print(self.name + "is studying for the test.")

    s1 = student("Harry", "17", "12th", "4.0")
    s2 = student("Roy", "17", "12th", "4.5")

    class Fighter:
        def _init_(self, name, strength, dexterity, vitality, magic):
            self.name = name
            self.strength = strength
            self.dexterity = dexterity
            self.vitality = vitality
            self.magic = magic