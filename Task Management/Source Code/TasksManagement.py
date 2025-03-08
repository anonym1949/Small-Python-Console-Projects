from ast import Try
from asyncio.windows_events import NULL
import csv
from datetime import date
import datetime
from genericpath import isfile
import io
import os
import sys
import time
from tkinter import Menu
from xmlrpc.client import DateTime



Path="CsvTasks.csv"



def CreateTasksFile(Path,Mode):
  CsvContent =False 
  try:
      CsvContent = open(Path,Mode,newline="") 
      CsvWriter = csv.writer(CsvContent,delimiter=",")
      CsvWriter.writerow(["TaskID","TaskName","TaskCategory","TaskDescription","TastStart DateTime","TastEnd DateTime","Priority","Status"])
      return True
  
  except FileExistsError:    
     return False;

  finally:
      if CsvContent:
       CsvContent.close()

def AddTaskToFile(List,Path):
  CsvContent = None
  try:
      CsvContent = open(Path,"a",newline="") 
      CsvWriter = csv.writer(CsvContent,delimiter=",")
      CsvWriter.writerow(List)
      return True
  except Exception as e:
       print(e) 
       return False
  finally:
      if CsvContent:
        CsvContent.close()

def CheckChoice(Op):   
      try :
          Operation = int(Op)
          if Operation <=0 or Operation>6:
              return 0
          else:
            return Operation    

      except Exception as E:
          return 0

def PrintHeader(ScreenName):
   print("="*63)
   print(" "*22,ScreenName)
   print("="*64)   
   print(" " *35,"|",time.ctime(),"|")
   print(" " *35,"="*28)
  
def PrintASingleTask(Header , List):
   print("===================================================")
   print(Header[0]," "*(18-len(Header[0])),":" ,List[0],sep="")
   print(Header[1]," "*(18-len(Header[1])),":" ,List[1],sep="")
   print(Header[2]," "*(18-len(Header[2])),":" ,List[2],sep="")
   print(Header[3]," "*(18-len(Header[3])),":" ,List[3],sep="")
   print(Header[4]," "*(18-len(Header[4])),":" ,List[4],sep="")
   print(Header[5]," "*(18-len(Header[5])),":" ,List[5],sep="")
   print(Header[6]," "*(18-len(Header[6])),":" ,List[6],sep="")
   print(Header[7]," "*(18-len(Header[7])),":" ,List[7],sep="")
   print("===================================================")

def ShowTasks(Path):
   os.system("cls")
   PrintHeader("T A S K S  L I S T")
   
   CsvContent=None
   try:
      CsvContent = open(Path,"r") 
      CsvReader = csv.reader(CsvContent,delimiter=",")
     
      if CsvReader != None:
        Row = next(CsvReader)
      
      Tasks =   list( CsvReader) 
      if Tasks == []:
         print("Vous n'avez aucune tache")
         return


      for item in Tasks:
         if item != []:
            print("\n")
            print("_"*100)
            print('|',Row[0],(20-len(Row[0]))*" ","|",item[0],"\n","_"*100,sep="")                                                 
            print('|',Row[1],(20-len(Row[1]))*" ","|",item[1],"\n","_"*100,sep="")          
            print('|',Row[2],(20-len(Row[2]))*" ","|",item[2],"\n","_"*100,sep="")
            print('|',Row[3],(20-len(Row[3]))*" ","|",item[3],"\n","_"*100,sep="")
            print('|',Row[4],(20-len(Row[4]))*" ","|",item[4],"\n","_"*100,sep="")
            print('|',Row[5],(20-len(Row[5]))*" ","|",item[5],"\n","_"*100,sep="")
            print('|',Row[6],(20-len(Row[6]))*" ","|",item[6],"\n","_"*100,sep="")
            print('|',Row[7],(20-len(Row[7]))*" ","|",item[7],"\n","_"*100,sep="")

              
   except Exception as e:
       print(e)
       return False

   finally:
      CsvContent.close()

def DataReader(message,Isdate=False):
   
   if Isdate:
    Data = input(message)
    try:
       userd = datetime.datetime.strptime(Data,'%Y-%m-%d %H:%M:%S')
       return userd
    except:
       return False
   else:
       Data = input(message) 
       return Data

def FindTask(Path):
   os.system("cls")

   PrintHeader("F I N D  T A S K")
   CsvContent=None
   IsFound=False
   try:
      CsvContent = open(Path,"r") 
      CsvReader = csv.reader(CsvContent,delimiter=",")
     
      if CsvReader != None:
        Row = next(CsvReader)
      
      Tasks =   list( CsvReader) 
      if Tasks == []:
         print("Vous n'avez aucune tache")
         return;
   

      TaskCode = DataReader("Entrez ID ou le nom du tache: ")
      for item in Tasks:
        if item !=[]: 
         if TaskCode in (item[0],item[1]):  
           IsFound=True
           PrintASingleTask(Row,item)
           break;
      
      if IsFound ==False:        
          print("ID ou le nom du tache non trouvez: ")


   except Exception as e:
           print(e)
           print("Erreur technique, veuillez reessayer plus tard :(")
   finally:
      CsvContent.close()   

def AddTask(Path):
   os.system("cls")
   PrintHeader("A D D  T A S K")
   print("\n")
   print("NOTE:Sauf(La date et L'heure Ces donnees ne sont soumises a aucune contrainte car elles vous sont propres."
         +"\nEcrivez ce qui vous convient dans chaque champ.\n")
   Tasks=[]

   Tasks.append(DataReader("Entrez ID de la tache (TaskID)                                      : "))
   Tasks.append(DataReader("Entrez le nom de la tache (TaskName)                                : "))
   Tasks.append(DataReader("Entrez la categorie de la tache (TaskCategory)                      : "))
   Tasks.append(DataReader("Entrez la description de la tache (TaskDescription)                 : "))
   print("Entrez maintenant la date et l'heure de debut et de fin de la tache  (Y-m-d H:M:S') ")
   
   Date1 = DataReader("Entrez la date et l'heure de debut de la tache                      : ")
   while Date1 ==False:
          Date1 = DataReader("Invalid Date Entrez la date et l'heure de debut de la tache         : ",True)

   Date2 = DataReader("Entrez la date et l'heure de debut de la tache                      : ")
   while Date2 ==False:
          Date2 = DataReader("Invalid Date Entrez la date et l'heure de Fin de la tache         : ",True)
          
   Tasks.append(Date1)
   Tasks.append(Date2)

   Tasks.append(DataReader("Entrez la priorite de la tache (Low /Medium/High)                   : "))
   Tasks.append(DataReader("Entrez le statut de la tache (Not Started /In Progress /Completed)  : "))

   choice =DataReader("Voulez-vous enregistrer cette tache oui/non?")
   if choice in ("yes","YES","OK", "OUI" ,"oui" ,"1" ,"TRUE" ,"true"):
      if AddTaskToFile(Tasks,Path):print("Fait avec succes :)");
      else :print("Erreur technique, veuillez reessayer plus tard :(")

def TaskModify(Path):
    os.system("cls")

    PrintHeader("T A S K   M O D I F I C A T I O N")
   
    CsvContent=None
    IsFound=False
    try:
      CsvContent = open(Path,"r") 
      CsvReader = csv.reader(CsvContent,delimiter=",")
     
      if CsvReader != None:
        Row = next(CsvReader)
      
      Tasks =   list( CsvReader) 
      if Tasks == []:
         print("Vous n'avez aucune tache")
         return;
      TaskCode = DataReader("Entrez ID ou le nom du tache: ")
      for item in Tasks:
        if item !=[] :
         if TaskCode in (item[0],item[1]):  
           IsFound=True
           PrintASingleTask(Row,item)

           choice =DataReader("Voulez-vous Modifier le statut de la tache Oui/Non? ")
           if choice in ("yes","YES","OK", "OUI" ,"oui" ,"1" ,"TRUE" ,"true"):
              Status = DataReader("Entrez le statut de la tache (Not Started /In Progress /Completed)  : ")
              item[7] = Status
              CreateTasksFile(Path,"w")
              for Record in Tasks:
                 AddTaskToFile(Record,Path)
              print("Fait avec succes :)")
           break



      if IsFound ==False:        
          print("ID ou le nom du tache non trouvez: ")


    except:
           print("Erreur technique, veuillez reessayer plus tard :(")
    finally:
      CsvContent.close()   

def DeleteTask(Path):

   os.system("cls") 
   PrintHeader("D E L E T E  T A S K")
   CsvContent=None
   IsFound=False
   try:
      CsvContent = open(Path,"r") 
      CsvReader = csv.reader(CsvContent,delimiter=",")
     
      if CsvReader != None:
        Row = next(CsvReader)
      
      Tasks =   list( CsvReader) 
      if Tasks == []:
         print("Vous n'avez aucune tache")
         return;
   

      TaskCode = DataReader("Entrez ID ou le nom du tache: ")
      for item in Tasks:
        if item !=[]: 
         if TaskCode in (item[0],item[1]):  
           IsFound=True
           PrintASingleTask(Row,item)

           choice =DataReader("Voulez-vous Supprimer cette tache oui/non? ")
           if choice in ("oui,yes"):              
              CreateTasksFile(Path,"w")
              for Record in Tasks:
                 if Record != item:
                  AddTaskToFile(Record,Path)
              print("Fait avec succes :)")
           break



      if IsFound ==False:        
          print("ID ou le nom du tache non trouvez: ")


   except:
           print("Erreur technique, veuillez reessayer plus tard :(")
   finally:
      CsvContent.close()   

def Manager(choice):
   match choice:
      case 1:
       ShowTasks(Path)
      case 2:
       FindTask(Path)
      case 3:
       AddTask(Path)
      case 4:
        TaskModify(Path)
      case 5:
          DeleteTask(Path)
 
def Menu():
   while True:
     os.system("cls") 
     PrintHeader("T A S K S  M A N A G E M E N T")
     print("\nBienvenue dans votre gestionnaire de taches :\n"+
           "Veuillez choisir une option :")
     print("="*40)
     print("Afficher les taches               [1]")
     print("Trouvez une tache les taches      [2]")
     print("Ajouter une tache                 [3]")
     print("Marquer une tache comme terminee  [4]")
     print("Supprimer une tache               [5]")
     print("Sauvegarder et quitter            [6]")
     print("="*40)
     print("Votre choix : ",end="")
     choice = CheckChoice(input());
     while choice ==0:
      choice = CheckChoice(input("Invalid Choice , Try Again: "))
     if(choice == 6):
           print(" C O M E  B A C K  S O O N")
           break;
     Manager(choice)
     input("\n press any key to back to main menu")



CreateTasksFile(Path,"x")
Menu()