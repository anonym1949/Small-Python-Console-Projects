
from ast import Dict
from functools import total_ordering
import json
import os
from random import choice
from sys import path
from textwrap import indent
import time


Path ="MenuFile.json"
CommandesList=[]

def CreateAFileWithMenu(Path,Mode):
    
    DictMenu ={
  "menu": {
    "categories": [
      {
        "name": "Entrées",
        "dishes": [
          { "name": "Salade César", "price": 8.5 },
          { "name": "Soupe du jour", "price": 5.0 },
          { "name": "Bruschetta", "price": 6.5 },
          { "name": "Carpaccio de Boeuf", "price": 9.0 },
          { "name": "Calamars Frits", "price": 7.5 }
        ]
      },
      {
        "name": "Plats Principaux",
        "dishes": [
          { "name": "Poulet Rôti", "price": 15.0 },
          { "name": "Saumon Grille", "price": 18.5 },
          { "name": "Pâtes Alfredo", "price": 12.0 },
          { "name": "Côte de Boeuf", "price": 22.0 },
          { "name": "Risotto aux Champignons", "price": 14.0 }
        ]
      },
      {
        "name": "Desserts",
        "dishes": [
          { "name": "Tiramisu", "price": 6.0 },
          { "name": "Fondant au Chocolat", "price": 7.5 },
          { "name": "Crème Brûlée", "price": 6.5 },
          { "name": "Macarons", "price": 5.5 },
          { "name": "Tarte Tatin", "price": 7.0 }
        ]
      },
      {
        "name": "Boissons",
        "dishes": [
          { "name": "Coca-Cola", "price": 2.5 },
          { "name": "Jus d'Orange", "price": 3.5 },
          { "name": "Thé à la Menthe", "price": 4.0 },
          { "name": "Cappuccino", "price": 4.5 },
          { "name": "Smoothie Mangue", "price": 5.0 }
        ]
      }
    ]
  }
}
    try:
       JsonPath = open(Path , Mode)
       json.dump(DictMenu ,JsonPath , indent=4)
       return True
    except :
        return False

def PrintHeader(ScreenName):
   print("="*63)
   print(" "*22,ScreenName)
   print("="*64)   
   print(" " *35,"|",time.ctime(),"|")
   print(" " *35,"="*28)
 
def CheckChoice(Op):   
      try :
          Operation = int(Op)
          if Operation <=0 or Operation>5:
              return 0
          else:
            return Operation    

      except Exception as E:
          return 0

def LoadDataFromJson(Path):  
  try:
     jsonFile = open(Path, "r")
     if jsonFile.read() =="":
          print("Menu Vide")
          return
     jsonFile.seek(0)
     JsonContent = json.load(jsonFile)   
     
     
  except ExceptionGroup as e:
      print(e)
      return None
  finally:
      jsonFile.close()
  return  JsonContent

def PrintMenu(JsonContent,isCommand=False):
     i=1 
     for category in JsonContent["menu"]["categories"]:
       print(" "*20,category["name"]," " *(20))   
       print("="*50)   
       print("|","Name"," "*24,"|price"," "*10)
       for dish in category["dishes"]:
         print("|",dish["name"]," "*(28- len(dish["name"])),"|",dish["price"],end="")
         if isCommand ==True:
            print(" "*7, "[",i,"]")
            i +=1
         else:print()   
        
       print("="*50)   
       print("\n")

def ShowMenu(Path):

  os.system("cls")
  PrintHeader(" R E S T A U R A N T  M E N U")
  jsonContent=LoadDataFromJson(Path)
  if jsonContent != None:
     PrintMenu(jsonContent)   
  else:
     print("No Menu For Today")

def FindCommandByCode(Path,ID):
   i=1
 
   JsonContent = LoadDataFromJson(Path)
   for category in JsonContent["menu"]["categories"]:     
       for dish in category["dishes"]:
         if ID == i:     
            return  dish
         else:
            i+=1
   return None

def ManageCommand(List):
   global CommandesList
   os.system("cls")
   PrintHeader("F A C T U R E ")
   
   Total =0
 
   for item in  List:
         print("Nom du repas  :",item["name"])
         print("Prix du Repas :",item["price"])
         Total += float(item["price"])
   print("="*30)
   print("Prix Total :",Total)
   choice =input("Voulez-vous confirmez oui/non? ")
   if choice not in ("oui","OUI"):
      return False
   else:
      print("Ajouté avec succès")
      CommandesList.extend(List)
      return True

def MakeACommand(Path):
   os.system("cls")
   PrintHeader("C O M M A N D E")
   jsonContent=LoadDataFromJson(Path)
   if(jsonContent !=None):
     PrintMenu(jsonContent,True)
   else :
      print("No Menu For Today")
      return
   try:
     ListOfCommands=[]
     while True: 
        ID= int(input("Entrez L'Id De Votre Commande ? "))
        while(ID<=0 or ID>20):
            ID=int( input("Invalid Choix ! Entrez L'Id De Votre Commande ? "))
        command = FindCommandByCode(Path ,ID)
        if(command !=None):
          ListOfCommands.append(command)
          
        choice =input("Voulez-vous ajouter une autre demande? oui/non ")
        if choice not in ("oui","OUI"):
           break
     if len(ListOfCommands)!=0:   
        
       if( ManageCommand(ListOfCommands)==False):
          raise BlockingIOError
       
        
     else:
        return
   except :
      print("Erreur ressayer Plus tard")
   
def DeleteACommand():  
   print("="*30)
   os.system("cls")
   PrintHeader(" D E L E T E  Y O U R  C O M M A N D S ")
   global CommandesList
   if len(CommandesList)==0:
      print("Vous n'avez aucune demande")
      return
   TempList=[] 
   for i in range(len(CommandesList)):
         print("="*30)
         print("Nom du repas  :",CommandesList[i]["name"])
         print("Prix du Repas :",CommandesList[i]["price"])
         choice= input("Voulez-vous supprimer cette demande? oui/non ")
         if choice not in("oui","OUI"):
            TempList.append(CommandesList[i])
            
         else:
             print("Suppression terminée avec succès")
             
   CommandesList =TempList
   print("="*30)
   






def ShowMyCommands():
   os.system("cls")
   PrintHeader("Y O U R  C O M M A N D S ")
   if len(CommandesList)==0:
      print("Vous n'avez aucune demande")
      return
   Total =0
   for item in CommandesList:
         print("="*30)
         print("Nom du repas  :",item["name"])
         print("Prix du Repas :",item["price"])
         Total += float(item["price"])

   print("="*30)
   print("Total =",Total)


def Manager(Op):
    match Op:
      case 1:
         ShowMenu(Path)  
      case 2:
          MakeACommand(Path)
      case 3:
          ShowMyCommands()
      case 4:
          DeleteACommand()

            
def Menu():
  while True :
   os.system("cls") 
   PrintHeader("R E S T A U R A N T ")
   
   print("\nBienvenue dans le restaurant !  :\n"+
         "Veuillez choisir une option :")
   print("="*40)
   print("Afficher le menu               [1]")
   print("Passer une commande            [2]")
   print("Voir l'addition                [3]")
   print("Supprimer une commande         [4]")
   print("Quitter                        [5]")
   print("="*40)
   choice =CheckChoice( input("Votre Choix ? "))
   while (choice ==0):
          choice =CheckChoice( input("Invalid Choix ! veuillez ressayer ? "))
          
   if choice ==5:
    print("A U  R E V O I R")
    break
   Manager(choice)
   input("press any key to go back ")
   
CreateAFileWithMenu(Path,"w")   
Menu()

