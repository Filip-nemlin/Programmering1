
import os
from pdb import Restart
import random
from colors import bcolors

while True:
    os.system('cls')


    print(bcolors.PURPLE + """
    -----------------------------------
    --- GISSA ETT TAL MELLAN  1-100 ---
    -----------------------------------
    ----- DU HAR TOTALT 7 FÖRSÖK! -----\n""")

    total_guesses = 0
    secret_number = random.randint(1,100)

    while total_guesses <= 7:
        try:
            guess=int(input(bcolors.CYAN + f"gissa ett tal mellan 1 och 100\n"))
        except ValueError: 
            print(bcolors.RED + f"du måste skriva ett tal utan decimaler\n")
            continue

        total_guesses += 1

        if guess == 0: 
            exit()

        if guess==secret_number: 
            print(bcolors.GREEN + f"du gissade rätt tal, det hemliga talet var {secret_number}.\ndet tog dig {total_guesses} försök.\n")

        elif guess > secret_number:
            print(bcolors.RED + f"du gissade för högt.\ndu har gissat {total_guesses} gånger.\ndu kan också ge upp genom att skriva 0\n")
        
        elif guess < secret_number:
            print(bcolors.RED + f"du gissade för lågt.\ndu har gissat {total_guesses} gånger.\ndu kan också ge upp genom att skriva 0\n")

        if total_guesses== 7:
            print(bcolors.RED + f"Du har tyvärr inte några försök kvar")

            again= input(bcolors.YELLOW + f"vill du försöka igen? Skriv J/N \n")
            if again == "J":
                break
            elif again == "N":
                exit()