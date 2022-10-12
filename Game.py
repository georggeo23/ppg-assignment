#import app
import Role1
import Role2
import random
import sys,time,os

def roleassign(doffy,choice):
 global Strength
 global Defense
 global Dexterity
 if doffy=='yes':
    if choice=='Bruiser':   #once the user has picked and confirmed their character, they will be assigned these attribute values
     Role2.assign()
     Strength=Role2.Strength
     Defense=Role2.Defense
     Dexterity=Role2.Dexterity
    if choice=="Mage":
     Role1.assign()
     Strength=Role1.Strength
     Defense=Role1.Defense
     Dexterity=Role1.Dexterity

def up(increase):
    global Strength
    global Dexterity
    global Defense
    match increase:
        case "Strength": 
         Strength+=1
         print("you're strength is increased by 1\n")
        case "Defense":
         Defense+=1
         print("you're Defensive capability is increased by 1\n")
        case "Dexterity":
         Dexterity+=1
         print("you're Dexterity is increased by 1\n")

counter=0
countere=0 
def Dicea():
    global roll1
    global counter
    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    print("Die two rolled "+ str(roll1))
    print("\nDie one rolled "+ str(roll2))
    counter+=roll1
    counter+=roll2
    
def Diceb():
    global roll1
    global counter
    roll1=random.randint (2,3)
    roll2=random.randint(2,3)
    print("\nDie one rolled "+str(roll1))
    print("\nDie two rolled "+ str(roll2))
    counter+=roll1
    counter+=roll2

def diceenemy():
    global countere
    global rollea
    global rolleb
    rollea=random.randint(1,5) 
    rolleb=random.randint(1,4)
    print("\nEnemy die two rolled "+ str(rollea))
    print("\nEnemy die one rolled "+ str(rolleb))
    countere+=rollea
    countere+=rolleb
    print('\n-*****************************************-')
    print("Your total roll count is "+ str(counter)+"\n")
    print("Your enemies total roll count is "+ str( countere)+'\n\n')
       