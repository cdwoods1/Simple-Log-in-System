userList = {}


def logIn():
    while True:
        userName = input("Please input your username: ")
        userPassword = input("Please input your password: ")
        if authenticationCheck(userName, userPassword):
            print("Access granted. Welcome.")
            break
        else:
            print("Wrong username/password. Please try again.")
            continue


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
