##Rock Paper Scissors Version 2
##VAMPIRE WARS!
##You challenge Nosferatu to a game of RPS. If you win, you get blood.
##If you lose, he gets yours. If you're drained, you die.
##By Amina Kombo

from random import randint

import sys

def printDivider():
    print("=================================================================")

def showStats():
    global name,myPints,nosPints
    print(name.upper(), ": ",myPints,"pints     NOSFERATU : ",nosPints,"pints")


def getOutcome():
    global myBet, nosBet
    outcome="It's a tie! Blood stays where it is. For now."
    ot=0
    if(myBet=="r" and nosBet=="p"):
        outcome="Paper covers rock. You lose."
        ot=-1
    elif(myBet=="p" and nosBet=="s"):
        outcome="Paper covers rock. YOU WIN!"
        ot=1
    elif(myBet=="p" and nosBet=="s"):
        outcome="Scissors cut paper. You lose."
        ot-=1
    elif(myBet=="s" and nosBet=="p"):
        outcome="Scissors cut paper. YOU WIN!"
        ot=1
    elif(myBet=="s" and nosBet=="r"):
        outcome="Rock breaks scissors. You lose."
        ot=-1
    elif(myBet=="r" and nosBet=="s"):
        outcome="Rock breaks scissors. YOU WIN!"
        ot=1

    print(outcome)
    return ot
        

def handlePlay():
    global myBet, myPints, nosPints,nosBet
    aNum=randint(1,3)
    if(aNum==1):
        nosBet="r"
    elif(aNum==2):
        nosBet="p"
    elif(aNum==3):
        nosBet="s"

    outcome=getOutcome()
    nosPints+=outcome*-1
    myPints+=outcome
    
    showStats()
    myBet=""

  
def gameOver():
    printDivider()
    global name, myPints, nosPints
    if(myPints>0):
        print("Your enemy begins to wither. And crawl.")
        print("You kick him away before he can pounce.")
        print("He lands as dust.")
        print("Nosferatu is no more.")
    else:
        print("Suddenly there is nothing.")
        print("Not even darkness.")

    print("                THE END")

    choice=""
    while(choice==""):
        choice=input("Play again? [y=Yes or n=No]: ")
        if(choice.lower()=="y"):
            name=""
            myPints=10
            nosPints=10
            openingMessage()
        elif(choice.lower()=="n"):
            exit
        else:
            gameOver()
    

def playGame():
    global myPints, myBet, nosPints
    while(myPints<20 and myPints>0):
        printDivider()
        if(myBet!="r" and myBet!="p" and myBet!="s"):
            myBet=input("Rock[r], Paper[p] or Scissors[s]? ")
        else:
            handlePlay()
    gameOver()


def openingMessage():
    global name
    printDivider()
    print("\n           VAMPIRE ROCK PAPER SCISSORS!\n")
    while(name==""):
        name=input("Tell us your name, Brave Soul: ")
        if(name.lower()=="nosferatu" or name.lower()=="dracula"):
            print("Lol. But no.")
            name=""
        
    printDivider()
    print(name.upper(),"vs","NOSFERATU\n")
    print("You Challenge Nosferatu to a game of RPS,",
              "with your blood as the bargain.")
    print("Whoever drains the other wins. You have 10 pints each.")
    playGame()
    


name=""
myPints=10
nosPints=10
myBet=""
nosBet=""

openingMessage()
