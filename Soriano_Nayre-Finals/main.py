import random

class Account:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accounts = {}
    
    def register(self, username, password):
        # self.accounts["username"] = self.username
        # print(f'{self.username} {self.password}')
        if username not in self.accounts:
            if self.accounts[username] == Account(username, password):
                print('Registered Successfully')
            # else:
            #     if len(password) < 4:
            #         print("Password too short")
        else:
            print('Already Taken')

    # def login(self, username, password):
    #     if username in self.accounts:
    #         self.accounts[username].password == password
    #         print("Login Successful")
    #         return self.accounts[username]
    #     else:
    #         print('Account not found')


while True:
    print("1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_username = input("Enter username: ")
        input_password = input("Enter passwoprd: ")
        Account.register("args", input_username, input_password)

        # created = Account.register
        # print(created)
    elif choice == '2':
        pass
    else:
        break

