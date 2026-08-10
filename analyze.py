from random_username.generate import generate_username

#Welcome User
def welcomeUser():
    print("\nWelcome to the Text-analysis Tool, I will help mine and analyse a body of text from a file you give to me")

#Get Username
def getUsername():
    #Print message prompting user to input their name
    usernameFromInput = input("\nTo begin, Please enter your username\n")

    if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
        print("Your username must be at least 5 characters long, alphanumeric only, have no spaces, and cannot start with a number")
        print("Assigning new username instead...")
        usernameFromInput = generate_username()[0]
        print(usernameFromInput)

    return usernameFromInput
    


#Greet the User
def greetUser(name):
    print("Hello, " + name)

def runProgram():
    welcomeUser()
    username = getUsername()
    greetUser(username)

runProgram()
