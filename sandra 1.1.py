import math
import random
import os    # kvoli otvaraniu suboru na MAC
import sys   # aby som mohol ukoncit program sys.exit()
             # kvoli oprave glitchu ukoncenia sandry, chyba
             # v prvej casti kodu

############################################################################
###                            S A N D R A                               ###
############################################################################

## hi mi kontroluje ci uz cast kodu prebehla, ak ano tak ju uz nevykonavam
## toto sa da spravit asi cez WRAPPER, pouzijem neskorej ked sa ho naucim
hi = False ##introduction=False
nm="" # potrebne kvoli volaniu funkcie v pododvetviach
def Sandra(hi,nm):
    count = 1
    gkw = ["game","play","chess","ludo","match"]
    ckw = ["calc","calculator","iterate","calculate","solve","math"]
    wkw = ["write","text","blog","type"]
    if hi == False :
        hi=True
        nm = str(input("Hi, what is yout name? "))
        print("Aloha,",nm,".My name is Sandra. How can i help?")
    cmd = str(input("Choose your command ,Today! "))

    if count == 1:
        if cmd.lower() in ckw:
            calculator(nm)    # calculator
        else:
            count+=1
    if count == 2:
        if cmd.lower() in gkw:
            games(nm)         # games center
        else:
            count+=1
    if count == 3:
        if cmd.lower() in wkw:
            writer(nm)        # txt writer/reader
            count=0
        else:
            print("I can't do that yet, im sorry :/, do you want "
                    +"to try again? \n Y for yes, N for no",nm," :)")
            xm=str(input())
            if xm.upper() =="Y" :
                Sandra(hi,nm)
            elif xm.upper() =="N" :
                print("Ok then, it was nice to meet you, have a nice day,"+
                    "Sandra out.")
                sys.exit()
    else:
        print("I can't do that yet, im sorry :/, do you want "
                    +"to try again? \n Y for yes, N for no",nm," :)")
        xm=str(input())
        if xm.upper() =="Y" :
            Sandra(hi,nm)
        elif xm.upper() =="N" :
            print("Ok then, it was nice to meet you, have a nice day,"+
                "Sandra out.")
            sys.exit()                
    

def writer(nm):
    print("Welcome to the writer",nm,".Here you can write stuff")
    fcm = str(input("Which file would you like to open?"))
    try :     
        ourFile = open(fcm + ".txt","a")
        cm = str(input("Would you like to write (w) or read (r) the file?"))
        if cm.upper() == "W": # appending mode (a)
##            of = open(os.path.expanduser("~/TextEdit/" + fcm + ".txt"))
            ourFile = open(fcm + ".txt","a")
            ourFile.write
        elif cm.upper() == "R":
##            of = open(fcm + ".txt" , "r")  # .rtf file v mac-u
            ourFile = open(fcm + ".txt","r")
            print(ourFile.read())
            ourFile.close()
    except :
        print("There is no such file, do you want to try again? Y/N")
        ccm = str(input())
        if ccm.upper() == "Y" :
            writer(nm)
        else :
            hi = True
            Sandra(hi,nm)
     
    hi = True
    Sandra(hi,nm)
    
def games(nm):
    def guess(nm):
        num = random.randint(0,10)
        print(nm," ",end="")
        cmnd = int(input("try to guess what number do i think.(0-10)"))
        if cmnd == num :
            print("Yes! You win.")
        else:
            print("I thought",num,)
            print("Care to try again? Y for yes, N for no")
            xm=str(input())
            if xm.upper() =="Y" :
                guess(nm)
            elif xm.upper() =="N" :
                games(nm)
    def anothergame(nm):
        print("What do you know, it works!")
        Sandra(hi,nm)
    def ludo(nm):
        x = int(input("Input size of the gameGrid. ( odd numbers)"))
        try:
            gameGrid = grid(x)
            hra_A_vs_B(gameGrid)
            hi = True
            Sandra(hi,nm)
        except:
            print("Sorry, Ludo code not included in this version,"+
                  "returning to main menu..")
            hi = True
            Sandra(hi,nm)
    
    print("Welcome to the Games Center",nm,",here will be some games lately"
          +", \nyou will be able to pick from several games.")
    ccmd= str(input("Enter the Game you want to play. :) "))
    if ccmd == "guess" :
        guess(nm)
    elif ccmd == "anothergame" :
        anothergame(nm)
    elif ccmd == "ludo" :
        ludo(nm)   
    else:
        print("──────▄▀▄─────▄▀▄\n"
          +"─────▄█░░▀▀▀▀▀░░█▄\n"
          +"─▄▄──█░░░░░░░░░░░█──▄▄\n"
          +"█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")

    hi=True
    Sandra(hi,nm)
    
def calculator(nm):
    print("Welcome to my calculator ",nm,", almost every function works till"
          +" you \ninput 0, then the function returns the result, have fun!")
    ccmd= str(input("Input + - % ^ * for mathematical operations."))
    if ccmd == "+":
        sSum=0
        a=int(input("input first number of sum: "))
        while a !=0:
            sSum+=a
            a=int(input("another one: "))
        print("The result of summation is: ",sSum,)
        hi=True
        Sandra(hi,nm)
    if ccmd == "-":
        dif=0
        a=int(input("input number to substract from: "))
        b=int(input("aand the substractor: "))
        dif=a-b
        print("The result of substraction is ",dif)
        hi=True
        Sandra(hi,nm)
    if ccmd == "*":
        multi=0
        a=int(input("input number to multiply: "))
        b=int(input("another one: "))
        while b !=0:
            multi = a*b
            a = multi
            b=int(input("another one: "))    
        print("The result of multiplication is: ",multi)
        hi=True
        Sandra(hi,nm)
    if ccmd == "%":
        divi=0
        a=int(input("input number to divie: "))
        b=int(input("input number to divide by: "))
        while b !=0:
            divi = a/b
            a = divi
            b=int(input("another one: "))    
        print("The result of division is: ",divi)
        hi=True
        Sandra(hi,nm)
    if ccmd == "^":
        result=0
        a=int(input("input number to raise: "))
        b=int(input("input the power: "))
        result=a**b
        print("The result is:",result)
        hi=True
        Sandra(hi,nm)
    else:
        print("Returning to main menu..")
        hi=True
        Sandra(hi,nm)
Sandra(hi,nm)




