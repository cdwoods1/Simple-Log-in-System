
loggingIn = True
while loggingIn:
    userName = input("Please input your username: ")
    userPassword = input("Please input your password: ")
    if userName == "cdwoods":
        if userPassword == "Stupidpeople1":
            print("Access granted. Welcome.")
            break
        else:
            print("Wrong username/password. Please Try again")
            continue
    else:
        print("Wrong username/password. Please try again.")
        continue
