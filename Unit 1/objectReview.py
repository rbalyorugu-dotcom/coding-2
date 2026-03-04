x = str("A class property is a varibale that stores data for a class.")
x = str("A class method is an action that a class performs via a function.")

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

    class Fighter:
        def _init_(self, Tifa, strength, dexterity, vitality, materia):
            self.Tifa = Tifa
            self.strength = strength
            self.dexterity = dexterity
            self.vitality = vitality
            self.materia = materia

        def attack(self, Tifa, strength):
            print('self.Tifa' + "threw 3 punches and one kick" + "with level 50 strength")

        def materia(self, Tifa, materia)
            if Tifa uses luck materia
                print("Luck is increased by 10%")

        def Limit Break(self, Tifa, strength)
            print("Tifa uses level 3 limit break")

            





            