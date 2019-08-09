import pickle
import os

filename: str = 'Users'

userList = {}

if os.path.getsize(filename) > 0:
    outfile = open(filename, 'rb')
    userList = pickle.load(outfile)
    outfile.close()

print(userList)


def logIn():
    tries = 0
    while tries < 4:
        userName = input("Please input your username: ")
        userPassword = input("Please input your password: ")
        if authenticationCheck(userName, userPassword):
            print("Access granted. Welcome.")
            return
        else:
            print("Wrong username/password. Please try again.")
            tries += 1
            continue
    print("You have attempted to login too many times. Please try again later.")


def authenticationCheck(username, password):
    if username in userList.keys():
        if password in userList.values():
            return True
        else:
            return False
    else:
        return False


def userCreation(username, password):
    userList[username] = password


def start():

    while True:
        userOption = input("Type 1 to login, 2 to create a new account, or 3 to change your password: ")
        if userOption == "1":
            logIn()
            infile = open(filename, 'wb')
            pickle.dump(userList, infile)
            infile.close()
            break
        elif userOption == "2":
            newUsername = input("Type in your new username: ")
            newPassword = input("Type in your new password: ")
            if newUsername not in userList.items():
                userCreation(newUsername, newPassword)
            else:
                print("This username already exists. Please try again.")
                continue
            input("Thank you very much.")
            continue
        elif userOption == "3":
            while True:
                oldUsername = input("Please confirm your current username: ")
                oldPassword = input("Please confirm your current password: ")

                if authenticationCheck(oldUsername, oldPassword):
                    newPassword = input("Please type your new password: ")
                    userList[oldUsername] = newPassword
                    break
                else:
                    print("No account was found. Please try again.")
                    continue
        else:
            print("You did not select either option. Please try again.")


start()
