# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 
print(x)
x = "A python class is the blueprint for creating objects. An object is what is created and instructed from the class."

# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.
print(x)
x = "An object property is a characteristic of an object. A method is the function of said object."

# 3. Create a unique python class. Your class should have 5 properties and 3 methods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter

class fitnessTracker:
    def __init__(self, name, age, weight, height, activitylevel):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.activitylevel = activitylevel

        def greet_user(self):
            print("Hello" + self.name + "Welcome to your fitness tracker")

        def bmi(self):
            print("self.weight" + "is" + "160 lbs" + "and" + "20lbs lighter" + "than" + "last month")

        def activity(self, activitylevel):
            print("self.activitylevel" + "is" + "high")

        def update_weight(self, new_weight):
            self.weight = new_weight