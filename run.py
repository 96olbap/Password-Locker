import string
from random import *
from user import User
from credentials import Credentials

def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user = User(username, password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_account_cred(accountName, accountUsername, accountPassword):
    '''
    Function that creates a new account's credentials
    '''

    new_account =  Credentials(acc-name, acc-username, acc-password)
    return new_account

def save_account(user):
    '''
    Function to save a user's account credentials
    '''
    user.save_credentials()

def delete_account(user):
    '''
    Function to delete a user's account credentials
    '''
    user.delete_credentials()

def find_account(username):
    return Credentials.find_by_username(username)

def display_accounts():
    return Credentials.display_credentials()

def main():

    print("Hello Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a new account, lg - Log in to your account")
        short_code = input().lower()
        if short_code == 'cu':
            print("Create account")
            print("-"*10)
            print ("Set username ....")
            username = input()
            print ("Set password ....")
            password = input()
            save_users(create_user(username, password))
            print('Account created successfully! Your accound details are as follows:')
            print("-"*10)
            print(f"Name: {username} \nPassword: {password}")
            print(f"\nUse your details to log into your account")
            print("\n \n")
        elif short_code == 'lg':
            print("Enter username...")
            loginusername = input()
            print("Enter your password:")
            loginpassword = input()
            if find_user(loginpassword):
                print("\n")
                print("Use these short codes : ca - create a another account, ve - View existing accounts")
                print("-"*60)
                choose = input().lower()
                if choose == 'ca':
                    print("Add your account credentials...")
                    print("-"*25)
                    accountUsername = loginusername
                    print("Acount name: eg twitter, instagram, etc")
                    accountName = input()
                    print("\n")
                    print("Use these short codes: g - Generate automatic password or cp - create your own new password")
                    decision = input()
                    if decision == 'g':
                        characters = string.ascii_letters + string.digits
                        accountPassword = "".join(choice(characters)for x in range(randint(6,16)))
                        print(f"Password: {accountPassword}")
                    elif decision == 'cp':
                        print("Enter your password:")
                        accountPassword = input()
                    else:
                        print("Kindly put in a valid choice")
                    save_account(create_account_cred(accountName, accountUsername, accountPassword))
                    print('\n')
                    print(f" Account Name:{accountName} \nUsername:{accountUsername} \nPassword:{accountPassword}")
                elif choose == 've':
                    if find_account(accountUsername):
                        print("Here is a list of your created accounts:")
                        print("-"*25)
                        for user in display_accounts():
                            print(f"Account: {accountName} \nPassword: {accountPassword} \n\n")
                    else :
                        print("Invalid credentials!")
                else:
                    print("Kindly put in a valid choice")
                    print("\n")
            else:
                print("Incorrect username or password, kindly try again! Thank you")
                print("\n")
        else:
            print("Kindly put in a valid choice")
            print("\n")



if __name__ == '__main__':
    main()