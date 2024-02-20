'''
Projekt 2.py: 

__author__  = "Filip Nemlin"
__version__ = "1.0.0"
__email__   = "filip.nemlin@elev.ga.ntig.se"
'''

from errno import ENAMETOOLONG
import os
from unicodedata import name
os.system("cls")

namelist=[]             #skapade en lista   
print(namelist)         #skrev ut listan


def edit_name(position, new_name):
    if position < len(namelist):
        namelist[position-1] = new_name     #definerar att redigera ett namn
    else:
        print(f"Position {position} finns inte i listan.")

def add_name(add):          
    namelist.append(add)    #definerar att lägga till ett namn

def remove_name(remove):
    if remove < len(namelist):
        namelist.pop(remove-1)      #definerar att ta bort ett namn
    else:
        print(f"Position {remove} finns inte i listan.")


while True:         #huvud loop

    print(namelist)

    action=input("Skriv 'add' om du vill lägga till ett nytt namn eller 'edit' om du vill ändra ett namn. Du kan trycka enter när som helst för att avsulta programet.\nsvar: ").lower()

    if action=="":
        print(namelist)
        break                   #gör så att man kan avsluta programet och se vilka namn som finns i listan när som helst genom att bara trycka enter

    elif action=="add":
        new_name=input("Skriv det namnet du vill lägga till\nsvar: ")
        add_name(new_name)      #om man skriver 'add' får man skriva in namnet man vill lägga till

    elif action=="edit":
        edit_option=input("Skriv 'remove' om du vill ta bort och 'change' om du vill ändra på något namn\nsvar: ").lower() #om man skrev 'edit' får man välja om man vill ta bort eller redigera ett namn

        if edit_option=="remove":
            remove=int(input("Skriv vilken position namnet du vill ta bort från listan har\nsvar: "))
            remove_name(remove)     #skriver in positionen på namnet man vill ta bort

        elif edit_option == "change":
            position = int(input("Skriv vilken position namnet du vill ändra i listan har\nsvar: "))    #väljer vilket namn man vill redigera
            if position < len(namelist):
                new_name = input("Skriv namnet som du vill att det ska ändras till\nsvar: ")    #skriver vad man vill att det nya namnet ska vara
                edit_name(position, new_name)
            else:
                print(f"Position {position} finns inte i listan.")      #felsökning om man skriver postionen på ett namn som inte finns
        