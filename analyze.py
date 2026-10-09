from random_username.generate import generate_username
from nltk.tokenize import sent_tokenize, word_tokenize
import re

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

# Extract sentences from raw text body
def tokenizeSentences(rawText):
     return sent_tokenize(rawText)

# Extract words from list of sentences
def tokenizeWords(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words

def extractKeySentences(sentences, searchPattern):
     matchedSentences = []
     for sentence in sentences:
          #if sentence matches desired pattern, add to matchedSentences
          if re.search(searchPattern, sentence.lower()):
               matchedSentences.append(sentences)
          return matchedSentences

#Get the average words per sentence, excluding punctuation
def getWordsPerSentence(sentences):
     totalWords = 0
     for sentence in sentences:
          totalWords += len(sentence.split(" "))
     return totalWords / len(sentences)
# Get User Details
    # welcomeUser()
    # username = getUsername()
    # greetUser(username)

#Extracting and Tokenizing text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = getWordsPerSentence(articleSentences)

#Get Analytics
stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getWordsPerSentence(articleSentences)

print("GOT:")
print(wordsPerSentence)
