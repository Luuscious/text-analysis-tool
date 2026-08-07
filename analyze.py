def welcomeUser():
    print("\nWelcome to the Text-analysis Tool, I will help mine and analyse a body of text from a file you give to me")

#Get Username
def getUsername():
    #Print message prompting user to input their name
    usernameFromInput = input("\nTo begin, Please enter your username\n")
    return usernameFromInput

#Greet the User
def greetUser(name):
    print("Hello, " + name)

def runProgram():
    welcomeUser()
    username = getUsername()
    greetUser(username)
    runProgram()

runProgram()
