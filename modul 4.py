import os
os.system('cls')

print("hello world")

print("hej och välkommen till grönalund, för att få åka måste vi veta hur lång du är!")
height=int(input("längd:"))
a=139
if height>a:
    print("du är tillräckligt lång för att åka!")
elif height<a:
    print("du är tyvärr för kort för att åka, välkommen tillbaka när du har växt!")

if height>a:
    print("vad heter du då?")
    name=input("namn: ")
    print("okej", name, "hur gammal är du?")
    age=input("ålder: ")
    print("vart bor du", name)
    home=input("jag bor i: ")
    print("okej vad roligt,", home, "är väldigt fint!")

