import random

class Account:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def register(self, username, password):
        print(f'{username} {password}')

        # # self.accounts["username"] = self.username
        # # print(f'{self.username} {self.password}')
        # if username not in self.accounts:
        #     if self.accounts[username] == Account(username, password):
        #         print('Registered Successfully')
        #     # else:
        #     #     if len(password) < 4:
        #     #         print("Password too short")
        # else:
        #     print('Already Taken')

    def login(self, username, password):

        if username == input_username:
           print("success")
           DiceGame.menu()
        else:
            print('Account not found')

class DiceGame:

    def play_game():
    
        user_score = 0
        cpu_score = 0

        rounds = 0

        
        
        while rounds == 3:
            cpu_roll = random.randint(1,6)
            user_roll = random.randint(1,6)
            print(f'cpu roll is {cpu_roll} \n user roll is {user_roll}')

            if user_roll > cpu_roll:
                user_score += 1
            elif cpu_roll > user_roll:
                cpu_score += 1
            else:
                print("it's a tie")
            
            cpu_roll = 0
            user_roll = 0
            rounds =+ 1

            break

        if user_score > cpu_score:
            print("you win")
            user_score +=3
        elif cpu_score > user_score:
            print("talo ka bobo")
        else:
            print("tabla")

        DiceGame.menu()
    def menu():
        while True:
            print("1. Start Game\n 2. See Leaderboard\n 3. Logout")
            menu_choice = input("Enter your choice: ")

            if menu_choice == '1':
                DiceGame.play_game()
            elif menu_choice == '2':
                pass
            elif menu_choice == '3':
                break
            else:
                print("wrong input")



while True:
    print("1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
        Account.register("self", input_username, input_password)
        
        # Account.register("args", input_username, input_password)

        # created = Account.register
        # print(created)
    elif choice == '2':
        login_username = input("login user: ")
        login_pass = input("login pass: ")

        Account.login("self", login_username, login_pass)



    else:
        break


