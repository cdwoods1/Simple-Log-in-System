import pickle
import os
from tkinter import *
from functools import partial

filename: str = 'Users'
userList = {}
logInAttempts = 0

# Tests to ensure that there is already saved accounts.
if os.path.getsize(filename) > 0:
    outfile = open(filename, 'rb')
    userList = pickle.load(outfile)
    outfile.close()


# Creates a new User on the database.
def userCreation(username, password):
    UserName = username.get()
    UserPassword = password.get()
    if UserName not in userList.keys():
        userList[UserName] = UserPassword


def authenticationCheck(username, password):
    if username in userList.keys():
        if password in userList.values():
            return True
        else:
            return False
    else:
        return False


def logInSuccessWindow():
    global logInAttempts
    logInAttempts = 0
    logInRoot = Tk()
    logInRoot.geometry("300x100")
    successLabel = Label(logInRoot, text="Access granted. Welcome.").place(x=20,y=30)


def logInFailureWindow():
    global logInAttempts
    logInAttempts += 1
    logInRoot = Tk()
    logInRoot.geometry("300x100")
    failureLabel = None
    if logInAttempts < 5:
        failureLabel = Label(logInRoot, text="Incorrect username/password. Please try again.").place(x=20, y=30)
    else:
        failureLabel = Label(logInRoot, text="You have attempted to log in too many times.").place(x=20, y=30)


def logIn(username, userpassword):
    UserName = username.get()
    UserPassword = userpassword.get()
    if authenticationCheck(UserName, UserPassword):
        logInSuccessWindow()
        return
    else:
        logInFailureWindow()
        return


def saveFile():
    infile = open(filename, 'wb')
    pickle.dump(userList, infile)
    infile.close()
    root.destroy()


def updatePassword():
    newRoot = Tk()
    newRoot.geometry("300x300")
    Reset = Label(newRoot, text="Please confirm your username and password.").place(x=20, y=30)
    NameTag = Label(newRoot, text="Username").place(x=20, y=60)
    passwordTag = Label(newRoot, text="Password").place(x=20, y=90)

    userNameTwo = StringVar()
    passWordTwo = StringVar()

    global authenticationCheck
    authenticationCheck = partial(authenticationCheck, userNameTwo.get(), passWordTwo.get())

    # The two entries are created.
    userNameEntryTwo = Entry(newRoot, textvariable=userNameTwo).place(x=80, y=60)
    passwordEntryTwo = Entry(newRoot, textvariable=passWordTwo).place(x=80, y=90)
    confirmationButton = Button(newRoot, text="confirm", command=authenticationCheck).place(x=20, y=120)


# The window is created.
root = Tk()
root.geometry("400x400")

# The tags are created next.
name = Label(root, text="Log In Screen").place(x=20, y=30)
userNameTag = Label(root, text="Username").place(x=20, y=60)
passWordTag = Label(root, text="Password").place(x=20, y=90)


userName = StringVar()
passWord = StringVar()

# The two entries are created.
userNameEntry = Entry(root, textvariable=userName).place(x=80, y=60)
passwordEntry = Entry(root, textvariable=passWord).place(x=80, y=90)

userCreation = partial(userCreation, userName, passWord)
logIn = partial(logIn, userName, passWord)
updatePassword = partial(updatePassword)

logInButton = Button(root, text="Log in", command=logIn).place(x=20, y=120)
createAccountButton = Button(root, text="Create Account", command=userCreation).place(x=70, y=120)
resetPasswordButton = Button(root, text="Reset Password", command=updatePassword).place(x=170, y=120)


def windowCreate():
    root.protocol("WM_DELETE_WINDOW", saveFile)
    root.title("Log In Screen")
    root.mainloop()


windowCreate()
