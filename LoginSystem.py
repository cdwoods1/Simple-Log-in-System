loggingIn = True

userNameList = []
passWordList = []

def logIn():
    while loggingIn:
        userName = input("Please input your username: ")
        userPassword = input("Please input your password: ")
        if userName in userNameList:
            if userPassword in passWordList:
                print("Access granted. Welcome.")
                break
            else:
                print("Wrong username/password. Please Try again")
                continue
        else:
            print("Wrong username/password. Please try again.")
            continue


def userCreation(username, password):
    userNameList.append(username)
    userNameList.append(password)

def start():
    while True:
        userOption = input("Type 1 to login and 2 to create a new account: ")
        if userOption == "1":
            logIn()
            break
        elif userOption == "2":
            newUsername = input("Type in your new username: ")
            newPassword = input("Type in your new password: ")
            userCreation(newUsername, newPassword)
            break
        else:
            print("You did not select either option. Please try again.")


