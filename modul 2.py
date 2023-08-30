import os


os.system('cls')

print("hello world")

x=2
y=7
print(x-y) #subtrahera
print(x+y) #addera
print(x/y) #dividera
print(x*y) #multiplicera
print(x//y)
print(x**y)

print("Det är jag som är Filip och du är?")
name=input("Namn:")
print("välkommen", name + ",", "hoppas du mår bra")

print("Men hur gammal är du då?")
age=input("ålder:")

print("okej så du heter",  name + ","" och är", age, "år gammal.")
print("Finns det något annat jag behöver veta om dig?")

other=input("annat:")
print("vad roligt", name)

print("skriv nu in två tal som ska multipliceras")
a=int(input ("tal 1:"))
b=int(input ("tal 2:"))
print(a/b)

print("nu tänkte jag att vi ska ta reda på om du är överviktig")
height=float(input ("Längd i cm:"))
weight=float(input ("vikt i kg:"))
height=height/100*2
bmi=weight/height
print("Du har", "%.1f" %bmi, "i bmi")

age=int(age)*52
print("förresten så har du levt i", age, "veckor")
