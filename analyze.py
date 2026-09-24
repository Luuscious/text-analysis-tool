from random_username.generate import generate_username

#Welcome User
def welcomeUser():
    print("\nWelcome to the Text-analysis Tool, I will help mine and analyse a body of text from a file you give to me")

#Get Username
def getUsername():

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:
        #Print message prompting user to input their name
            inputPrompt = ""
            if attempts == 0:
                 inputPrompt = "\nTo begin, Please enter your username:\n"
            else:
                 inputPrompt = "\nPlease try again:\n"
            usernameFromInput = input(inputPrompt)

            #Validate username
            if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
                print("Your username must be at least 5 characters long, alphanumeric only, have no spaces, and cannot start with a number")
            else:
                 return usernameFromInput

            attempts += 1

    print("\nExhausted all " + str(maxAttempts) + " attempts, Assigning new username instead...")
    return generate_username()[0]
    

#Greet the User
def greetUser(name):
    print("Hello, " + name)

#Get text from file
def getArticleText():
     f = open("files/article.txt", "r")
     rawText = f.read()
     f.close()
     return rawText.replace("\n", " ").replace("\r", "")

# def runProgram():
#     welcomeUser()
#     username = getUsername()
#     greetUser(username)

# runProgram()

articleTextRaw = getArticleText()
print("GOT:")
print(articleTextRaw)
