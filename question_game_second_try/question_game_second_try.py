# Question - Answer Game            started on 02.03.2023, took a day or smthn dont remember tbh
# 
# copyright: ENES SOYLU             use each and every line of code as you wish mate!

from time import sleep # sleep method is going to be used later for a couple times, need to import it
import random # random's methods are going to be used a couple times, that's why we needed to import it as well

def listStart(): # each time user chooses to play again, lists are going to be available to reuse with this function

    global questionsList, answersList, correctAnswers          # all these lists are being declared globally
    global answersOfUser, decisionAndAnswer, lettersList       # to be available to use with other functions

    global points # same as the lists
    points = 0

    questionsList= ["What is Enes's name?", # the list where we have the questions
                    "How old is Enes?",
                    "When was Enes born?",
                    "What is Enes's major?"]

    answersList = [["Enes", "Ahmet", "Behcet", "Cemal"], # and the list where we have the answers
                   ["20", "21", "22", "23"], 
                   ["2002", "2003", "2004", "2005"], 
                   ["CS", "Biologist", "Doctor", "Physicist"]]

    correctAnswers = [] # to make it a bit more challenging i used the correct answers also in the answers list
                        # that's why correct answers have to be detected somehow, and those answers are going to be
                        # listed in this very list

    answersOfUser = []  # user's answers are going to be listed here

    lettersList = ["A", "B", "C", "D"] # each answer is going to be represented with a letter
                                         # and these letters also are going to be used to get user's answers

    decisionAndAnswer = [[],[],[],[]] # answers and letters(as decisions) are going to be 
                                      # listed in this nested list

def decisionsPrint(iterator): # basically to print the letters
    return lettersList[iterator]

def answersPrint(i): # prints the answers in alphabetic order
    for j in range(0,4):
        random.shuffle(answersList[j]) # shuffles the list to get the answers in a random order each time program runs
        global decisionAndAnswer
        decisionAndAnswer[i].append((str(decisionsPrint(j)) + ". " + answersList[i][0])) # combines letters with answers
        print(decisionAndAnswer[i][j])
        answersList[i].pop(0) # deletes the current answers from its list to use each answer only for once

def answersInput(): # to get user's response
    global questionS_Answer
    questionS_Answer = str(input("\nPlease enter your answer: ")).upper() # either user enters lower or upper case
    return questionS_Answer                                               # it isn't going to make any difference

def decisionAndAnswerEdit(i): # since the letters are separate from the answers at the beggining to mix the answers and to keep
    for j in range(0,4):      # the letters in alphabetic order, they were supposed to get together, and get separated again
        if decisionAndAnswer[i][j][3:] == "Enes":
            correctAnswers.append(decisionAndAnswer[i][j][0])
        elif decisionAndAnswer[i][j][3:] == "20":
            correctAnswers.append(decisionAndAnswer[i][j][0])
        elif decisionAndAnswer[i][j][3:] == "2002":
            correctAnswers.append(decisionAndAnswer[i][j][0])
        elif decisionAndAnswer[i][j][3:] == "CS":
            correctAnswers.append(decisionAndAnswer[i][j][0])

def decisionAndAnswerCheck(i): # checks if user's answers matches with the correct letters
    global points
    if answersOfUser[i] == correctAnswers[i]:
        print("Correct!")
        points += 1 # adds point to keep the amount of correct answers, which is going to be used at the end of the game
    else:
        print("Wrong!")

def questionsPrint(): # this function was originally created just to print questions but i was too lazy to
    print("\n")       # create new funcs, and i just used this one to do more than it was meant to be
    for i in range(0,4):
        print("\n---------------------------\n")
        print(questionsList[0])
        questionsList[0]
        questionsList.pop(0)                          # this part prints the questions and answers with a
        print("")                                     # user friendly UI (well, kinda user friendly)
        answersPrint(i)
        answersOfUser.append(answersInput())
        decisionAndAnswerEdit(i)
        decisionAndAnswerCheck(i)
    print("\n---------------------------")

def pointPrint(): # prints your total score
    print("\nYou have answered {} out of 4 questions correctly".format(points))
    print("\n---------------------------")

def gameStartQuestion(again, correctly): # asks users if she'd like to play for the first time or again if she already played
    global userAnswer
    userAnswer = str(input("\nWould you like to play" + again + "?" + correctly + "(yes, no): ")).lower()
    if again == " again":
        listStart()
    return userAnswer

def gameOpening(): # some simple UI stuff for start of the game
    sleep(0.75)
    print("\n\n\t---------------------------")
    print("\n\n\t\tGame Starts\n\n")
    print("\t---------------------------\n")
    sleep(0.75)
def gameEnding(): # some simple UI stuff for end of the game
    sleep(0.75)
    print("\n\n\t---------------------------")
    print("\n\n\t\t Game Ends\n\n")
    print("\t---------------------------\n")
    sleep(0.75)

def startQuestionCheck(): # checks if user wants to play or if her answer is accurate
    startQuestionControl = True
    while startQuestionControl:
        if userAnswer == "yes":
            listStart()
            gameOpening()
            questionsPrint()
            pointPrint()
            gameStartQuestion(" again","")
        elif userAnswer == "no":
            gameEnding()
            startQuestionControl = False
        else:
            gameStartQuestion("", " (Please enter a valid value) -> ")

def game():                     # since i was too lazy to create more spesific funcs,
    gameStartQuestion("","")    # this one did not get too crowded, that's why seems a bit unnecessary tbh
    startQuestionCheck()

game() # and there we go