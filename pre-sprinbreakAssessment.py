class Smartphone:
    def __init__(self, brand, user, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def charge_battery(self):
        self.battery_level = 50
        print("Battery level is now at " + str(self.battery_level) + "%")
        
        while self.battery_level < 100:
            response = input("Do you want to charge your phone? ")
            if response.lower() == "yes":
                print("adding 10% to battery level")
                self.battery_level += 10
                print("Battery level is now at " + str(self.battery_level) + "%")
            else:
                break


def multiply_x(5):
    x =  range(1,11)
    for n in x:
        print(number * n)

multiply_x(5)


def insert_dollars(amount):
    if user insert_dollars_dollars += 1:
        print("You have inserted " + str(amount) + " dollars.")
        print("You will receive " + str("4 quarters") + " in change.")

insert_dollars()

def travelDiscount_eligibility():
    if user has booked a room and a plane ticket:
        print("Congratulations! You are eligible for a gold travel discount.")
    elif user has booked a room or a plane ticket:
        print("Congratulations! You are eligible for a silver travel discount.")
    else:
        print("Sorry, you are not eligible for a travel discount at this time.")

travelDiscount_eligibility()                