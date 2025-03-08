


import os
import random
import time

UserName=""
def PrintHeader(ScreenName,User=""):
   print("="*63)
   print(" "*22,ScreenName)
   print("="*64)
   if User !="":
     print(" " *35,"|",time.ctime(),"|")
     print(" " *35,"="*28)
     print(" "*35 ,"|UserName :",User,' '*(13-len(User)),"|")
     print(" " *35,"="*28)
   else:
     print(" " *35,"|",time.ctime(),"|")
     print(" " *35,"="*28)

def UserWelcome():
   print("\n")
   print("Veuillez enter ton nom :",end="");
   Name= input()
   global UserName 
   UserName = Name
   print("="*111)
   print("Bienvenue" ,Name.upper(),"je suis un programme intelligent Je vais jouer avec toi le jeu (Vrai, Passe, Faux]")
   print("!Jai choisi un nombre secret a 4 chiffres differents.""")
   print("="*111)
   print("Vous avez 5 tentatives pour trouver nom nombre. \nEst-ce vous etes prets :oui/non ",end="")
   choice = input()
   if choice in ("yes","YES","OK", "OUI" ,"oui" ,"1" ,"TRUE" ,"true"):
       return True

   return False;

def SetupGameEnviromment():
   global UserName
   PrintHeader("G A M E  [Vrai, Passe, Faux]",UserName)
   if UserWelcome():
      os.system("cls")
      PrintHeader("G A M E  [Vrai, Passe, Faux]",UserName)
 
def Read4NumbersOnly(message):

    Num =input(message)
    if len(Num) != 4:
       return False;
    try:
        int(Num)
    except :
       return False

    for i in range(0,4):
       for j in range(0,4):
          if i != j:
             if Num[i] == Num[j]:
                return False
       
    ListOfNumbers=[]        
    for i in range(0,4):       
       ListOfNumbers.append( int(Num[i]))

    return ListOfNumbers      

def GenerateRandomNumber():
 
  ListOfNumbers=[]
  ListOfNumbers.append(random.randrange(0,10))
  for i in range(0,3): 
    Num = random.randrange(0,10)
    while Num in ListOfNumbers:
        Num = random.randrange(0,10)
    ListOfNumbers.append(Num)
  return ListOfNumbers 

def Comparaison(User ,computer):
   
   ListResult=[]
   for i in range(0,len(User)): #4
      if User[i] == computer[i]:
         ListResult.append("vrai")
      elif User[i] in computer:
         ListResult.append("passe")
      else:
         ListResult.append("faux")


   return ListResult

def CheckIFUserWin(List):
   
   AllAreVrai=False
   for i in range(0,len(List)):#4
      if List[i] =="vrai":
         AllAreVrai=True
         continue
      else:
         AllAreVrai=False
         return AllAreVrai 
   return AllAreVrai   

def Game():
   
  ComputerNumber = GenerateRandomNumber()
  Try =0
  IsUserWin=False

  while (Try <5):
    print("="*55)
    print("Tentative N :[",Try+1,"]")
    UserNumber = Read4NumbersOnly("Entrez un nombre a 4 chiffres : ")
    while UserNumber ==False:
       UserNumber=Read4NumbersOnly("Invalid Choix Entrez un nombre a 4 chiffres : ")
    Try +=1   
    ListOfResults = Comparaison(UserNumber,ComputerNumber)   
     
    print("Result  :")
    for i in range(0,4):
       print(UserNumber[i],"(",ListOfResults[i],")")
    if CheckIFUserWin(ListOfResults):
       print("Congratulations! You found the secret number: ","".join(map(str ,ComputerNumber)))
       print("="*55)
       break;
         
    if(Try ==5):
      print("Sorry, you didn't find the secret number. The number was: ","".join(map(str ,ComputerNumber)))
      print("="*55)



def Start():
  global UserName
  os.system("cls") 
  SetupGameEnviromment()
  Game()
  
  while True: 
   choice = input("Voulez-vous jouer une autre partie ? (oui/non) ")
   if choice  in ("yes","YES","OK", "OUI" ,"oui" ,"1" ,"TRUE" ,"true"):
    os.system("cls")
    PrintHeader("G A M E  [Vrai, Passe, Faux]",UserName)
    Game()
   else: 
     print("AU  R E V O I R :(")
     break;




Start()