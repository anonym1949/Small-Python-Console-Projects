from ast import Not
import datetime
from decimal import DivisionByZero
from os import system
import os
from sqlite3 import Date
import time


History=[]
Log=datetime.datetime.today()
def ShowHistory():
   print("Your log Time :",Log)
   
   if(len(History)==0):
      print("You Have No History")
      return
   print("Your Operations :");
   for item in History:
      print(item)

def Calculation(Num1 , Num2 , Op):
    match (Op):
         case "+":
            return Num1 + Num2
        
         case "-":
            return Num1 - Num2
        
         case "*":
            return Num1 * Num2
        
         case "/":
            if(Num2 == 0):
                return ( " Error : DivisionByZero")
            return Num1 / Num2
        
         case "**":
            return Num1 ** Num2
        
def PrintHeader():
   print("="*63)
   print(" "*22,"C A L C U L A T O R")
   print("="*64)
   
   print(" " *35,"|",time.ctime(),"|")
   print(" " *35,"="*28)

def CheckChoice(Op):   
      try :
          Operation = int(Op)
          if Operation <=0 or Operation>7:
              return 0
          else:
            return Operation    

      except Exception as E:
          return 0

def ReadNumber(Message):
    try: 
       X =float(input(Message))
       return X
    except:
        return "ErrorDeConversion"

def ReturnOpSymbol(OpNumber):
    match (OpNumber):
         case 1:
            return  '+' 
        
         case 2:
            return  '-' 
        
         case 3:
            return  '*' 
        
         case 4:
            return  '/'
        
         case 5:
            return  '**' 

def PrintHeaderForCalculation(Operation):
   os.system("cls")
   print("="*63)
   print(" "*22,"Make Your Calculation [{}]".format(ReturnOpSymbol(Operation)))
   print("="*64,end="\n\n")

def ManageFirst5Choices(Operation):

 while True:
   os.system("cls")
   PrintHeaderForCalculation(Operation)

   Num1 = ReadNumber("Entrez Le Premier Nomber  ?")
   while Num1 =="ErrorDeConversion":
      Num1 = ReadNumber("Invalid Nomber >>> Entrez Le Premier  Nomber ?")
      
   Num2 = ReadNumber("Entrez Le Deuxieme Nomber ?")
   while Num2 =="ErrorDeConversion":
      Num2 = ReadNumber("Invalid Nomber >>> Entrez Le Deuxieme Nomber ?")
       
   result = Calculation(Num1,Num2,ReturnOpSymbol(Operation))
   HST ="{} {} {} = {}".format(Num1,ReturnOpSymbol(Operation),Num2 ,result)
   History.insert(0,HST)
   print(" {} {} {} = {}".format(Num1,ReturnOpSymbol(Operation),Num2,result))   

   choice =input("Do You Want To Make Another Operation Yes/No ")
   if (choice not in ("yes","YES","1","oui","ok","OK","vrai","VRAI")):
         break;

def PrintHeaderForHistory():
   os.system("cls")
   print("="*63)
   print(" "*22," Your History ")
   print("="*64,end="\n\n")

def ManageChoiceN6():
 
 PrintHeaderForHistory()
 ShowHistory()
 
 choice=input("Press Any Key To Go Back To Main Menu ")
 
def Menu():
  while True:  
   os.system("cls")
   PrintHeader()
   print("\nplease choose your operaction :")
   print("="*40)
   print("Addition        [1]")
   print("Substraction    [2]")
   print("Multiplication  [3]")
   print("division        [4]")
   print("Puisons         [5]")
   print("History         [6]")
   print("Quitter         [7]")
   print("="*40)
   print("Vote Choix ? ",end="")
   Operation = CheckChoice(input())
   while (Operation == 0):
          Operation = CheckChoice(input("Invalid Choice , Try Again: "))

   if Operation >=1 and Operation<=5:
       ManageFirst5Choices(Operation)
       
   elif Operation==6:
     ManageChoiceN6()
   else:
      break;

#start
Menu() 

