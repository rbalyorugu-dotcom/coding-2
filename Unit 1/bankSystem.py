class IanFirstBank:
    def_init_(name, self, password, address, balance):
        self.name = name
        self.password = password
        self.address = address
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('thanks '+ self.name +'your new balance is ' + str(self.balance))

    def withdraw(self, balance, amount):
        self.balance -= amount
        print('thanks '+ self.name + 'your new balance is ' + str(self.balance))

    def encryptionMiddleware(self, name, password, password):
        password = 123ABC
        encrypt = 

    def closeBankAccount(self):


    def accessAccount(self, name, password):
        print('')
        # send all user info

    def transfer(self):
        print('')

account_1 = IanFirstBank('John', '123ABC', 'NA', 100)
account_2 = IanFirstBank('Ashley', '321ABC', 'NA', 200)

account_1.deposit(50)
account_2.withdraw(60)

def createAccount():
    print("Welcome to Ian's first bank.")
    print("please complete the following questions to create your account: ")
    name = input("name: ")
    password = input("password: ")
    address = input("address: ")
    balance = input("How much would you like to add to the new account?: ")

print("Congratulations! Your bank account is done.")

    account_3 = IanFirstBank(name, password, address, balance)
    users.append(account_3)

createAccount()