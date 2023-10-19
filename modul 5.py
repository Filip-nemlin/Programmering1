from ast import Delete
import os
os.system('cls')

persons =["Filip", "Eric", "Hannes", "Simon", "Victor", "Viktor", "David"]

for i in persons:
    print(i)

print("\n\n\n")

persons[3]="Simone"
for i in persons:
    print(i)

print("\n\n")
while True:

    new_person=input("lägg till en ny person i listan, tryck enter om du är klar med att lägga till: ")
    if new_person=="":
        break
    for i in persons:
        print(i)
    persons.append(new_person)

count=len(persons)
print(f"det finns totalt {count} personer i listan")


while True:

    x=int(input(f"skriv in ett nummer mellan 1 och {count} som du vill ta bort från listan, tryck enter när du känner dig nöjd: "))
    if x=="":
        break
    for i in persons:
        print(i)
        
    persons.pop(x-1)
