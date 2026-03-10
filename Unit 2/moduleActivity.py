#What is a phython module/library?
"A python module/library is a collection of unique functions that are already written for us to use."

import userModule_p2

userModule_p2.drive()

car1 = userModule_p2.CarModel("red", "Ferrari F80", "50 mph")
car2 = userModule_p2.CarModel("blue", "Lamborghini Aventador", "60 mph")

print(car1.color)
car2.speed()
car1.speed()

print(userModule_p2.grades)