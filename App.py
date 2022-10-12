import Game
import Role1
import Role2

def trdoffy():
      global doffy
      print("\nType yes to continue and no to retry\n")
      doffy=input(str("")).lower().strip()
      while doffy !='yes' and doffy !="no":
        print("Try again\n")
        print("Type yes to continue and no to retry\n")
        doffy=input(str("")).lower().strip()

def name():
    print("Please enter your name: \n")
    Pname= input(str(""))
    
def question():
    global choice
    print("Bruiser or Mage\n")
    print("Bruiser Stats:\nStrength =4 Dexterity =3 Defense =2\n")
    print("Mage Stats:\nStrength =3 Dexterity =2 Defense =4\n")
    choice= input(str("")).lower() #Offers the option of Bruiser or Mage

def wrongchar():
    question()
    while choice !="Bruiser" and choice !='Mage':#ensures that the user has picked one the options 
      print ("please input one the given options\n")
      question()
    if choice=="Bruiser" or choice=="Mage":#if the user has picked one of the options it will continue
        print('You have picked ' + str(choice) +' is this the character you wish to choose?')

def inc(): 
      global increase
      print("\nWould you like to increase the stat, Defense, Strength, Or Dexterity?\n")
      increase=input(str(""))
      while increase !='Strength' and increase!="Defense" and increase!="Dexterity":
        print ("please input one the given options\n")
        print("\nWould you like to increase the stat, Defense, Strength, Or Dexterity?\n")
        increase=input(str(""))

def winorlose():
    if counter<countere:
     print("you lose\n")
    if counter>countere:
     print("you win\n")

def check():
    print('\nYour stats are \nStr='+ str(Game.Strength)+'\nDex='+ str(Game.Dexterity)+ '\nDefense=' +str(Game.Defense)+"\n")

#-------------------------------------------------------------------------------------------------------------------------------
print("Welcome to Atlas\n") 

#app
name()
trdoffy()
while doffy=='no':
   name()
   trdoffy()  

wrongchar()
trdoffy()
while doffy=='no':
    wrongchar()
    trdoffy()

print("You are a "+ choice +''' in the kingdom of atlas.The year id 1975, in the indutrial revolution.    
    Your country is at war with the neighbouring and you have been asked for aid. This is your chance to show your worth. 
    Rise up and take a stand.\n''')
print("\nIn order to win this battle, you will have to pass three various trials")
print("\nThe first challenge is one that requires you to gather resources.\n")
print("\nThe second trial is for you to craft items with these resouces\n")
print("\nThe third trial is to slay enemies .\n")

Game.roleassign(doffy,choice)

print('\nyou come across your first fight\n')
print('''\nChoice a: \nRoll two dice with values from 1-6. 
    \nChoice b:\nRoll two dice with values ranging from 2-3 and a +1 increase to any attribute of your choice.
    \nChoice c: \nNo roll, but 2 point increase in an attribute of your choice\n''')
print('\nIn order to win each challenge, you must roll the dice three times and finish the challenge with a higher score than that of your enemies\n')
print('Winning a challenge by a margin of less than 5 will result in the increase of a stat based on the\n type of challenge\n')
print("However print losing a challenge by a margin of less than 5 will result in the decrease of a stat based on the type of challenge\n")
print('Winning the challenge by a margin of 5 of greater will increase a stat by 2 depending on the type of challenge.\n') 
print('However, losing by a margin of 5 or greater will result in the decrease of a stat by 2\n')
print('You must have a total of 5 points in each stat in order to win. Any stat less than 5 will result in a loss\n')
def dicechoice():
    global toss
    print("\nWould you like to roll dice a or dice b or c\n")
    toss=input(str(""))
    while toss!= "a" and toss!="b" and toss!="c":
        print("please input a,b ,or c\n")
        print("Would you like to roll dice a or dice b or no roll\n")
        toss=input(str(""))


def ffight():
    times=0
    global counter
    global countere
    Game.counter=0
    Game.countere=0
    while times<=2:
     dicechoice()
     trdoffy()
     while doffy=='no':
        dicechoice()
        trdoffy()
     if doffy=="yes":
        match toss:
         case "a":
          Game.Dicea()
          counter=Game.counter 
          times+=1
         case "b":
            Game.Diceb()
            counter=Game.counter 
            check()
            inc()
            trdoffy()
            while doffy=="no":
             check()
             inc()
             trdoffy()
            if doffy=="yes":
             Game.up(increase)
            check()
            times+=1
         case "c":
            print("you've decided to not roll and instead increase two values\n")
            check()
            inc()
            trdoffy()
            while doffy=='no':
             check()
             inc()
             trdoffy()
            Game.up(increase)
            check()
            inc()
            trdoffy()
            while doffy=='no':
             check()
             inc()
             trdoffy()
            Game.up(increase)
            check()
            times+=1
        Game.diceenemy()
    #print("Your total roll count is "+ str(counter)+"\n")
    countere=Game.countere
            
check()
print ('you are entering the first fight. This is a test of Health. Depending on the outcome of this game, \nyou may lose Defense or gain Defense')

ffight()
winorlose()
if countere>counter:
 if countere-counter>=5:
    Game.Defense-=2
    print("\nCritical loss, a -2 decrease in Defense\n")
 else:
    Game.Defense-=1
    print("\nYou suffered a Loss, a -1 decrease in Defense\n")
else:
 if counter-countere>=5:
    Game.Defense+=2
    print("\nMassive Win, +2 increase in Defense\n")
 else:
    Game.Defense+=1
    print("\nYou win, +1 increase in Defense\n")


check()
print("--------------------------------------------")
print('''You are entering the second fight. This is a test of Strength. Depending on the outcome of this game, you may lose Strength or gain Strength''')
ffight()
winorlose()
if countere>counter:
 if countere-counter>=5:
    Game.Strength-=2
    print("\nCritical loss, a -2 decrease in Str\n")
 else:
    Game.Strength-=1
    print("\nYou suffered a loss, a -1 decrease in Str\n")
else:
 if counter-countere>=5:
    Game.Strength+=2
    print("\nMassive win, a +2 increase in Str\n")
 else:
    Game.Strength+=1
    print("\nYou won, a +1 increase in Str\n")
check()
print("--------------------------------------------")
print('''You are entering the third fight. This is a test of dexerity. Depending on the outcome of this game, \nyou may lose Dexterity or gain Dexterity''')

ffight()
winorlose()
if countere>counter:
 if countere-counter>=5:
    Game.Dexterity-=2
    print("\nyou have suffered a critical loss, a -2 decrease in Dex\n")
 else:
    Game.Dexterity-=1
    print("\nyou have suffered a loss, a -1 decrease in Dex\n")
else:
 if counter-countere>=5:
    Game.Dexterity+=2
    print("\nMassive win, a +2 increase in Dex\n")
 else:
    Game.Dexterity+=1
    print("\nYou Win, a +1 increase in Dex\n")
check()

if Game.Defense<5 or Game.Strength<5 or Game.Dexterity<5:
    print('you lost. Restart the game to try again')
if Game.Defense>=5 and Game.Strength>=5 and Game.Dexterity>=5:
    print('Excelsior! You Won!!!!!!')