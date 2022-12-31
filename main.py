#~~~ Pratham-code ~~~
#~~ IMPORT ~~
import os
import time
from getpass import getpass
from bank import *

#~~ MENU ~~
menu1 = ("1)Coffee = 15\n2)Ice-Coffee = 20\n")

#~~ DEF ~~
def coffee(id1):
    print(menu1)
    cid = input(f"Hello {id1} which coffer you want\n")

#~~ Coffee ~~
    if cid == '1':
        input("total 15 for pay press enter")
        total1 = (Prathampay - 15)
        if total1 >= 0: 
         f = open(f"bank.py", "w")
         f.write(f"Prathampay = {total1}")
         f.close()
         time.sleep(2)
        else:
          print('not found')
          time.sleep(2)

#~~ Ice-Coffee ~~
    elif cid == '2':
        input("total 20 for pay press enter")
        total1 = (Prathampay - 20)
        if total1 >= 0: 
         f = open(f"bank.py", "w")
         f.write(f"Prathampay = {total1}")
         f.close()
         time.sleep(2)
        else:
          print('not found')
          time.sleep(2)

#~~ cappuccino ~~
    elif cid == '3':
     pass

    elif cid == 'exit':
      os.system('cls')
      print("exit")
      time.sleep(1)
      os.system('cls')
      print("exit from shop")
      exit()

    elif cid == 'addm':
        addm = input("add $")
        add1 = int(Prathampay) + int(addm)
        f = open(f"bank.py", "w")
        f.write(f"Prathampay = {add1}")
        f.close()

    else:
      print("not found")


while True:
 os.system("cls")
 id1 = "Pratham"
 coffee(id1)


#~~ MAIN-CODE ~~
print("Welcome To Coffee Shop")
print("Please login your account")

id1 = input("user\n")
if id1 == "Pratham":
   password = getpass("~~ Password ~~\n")
   if password == '2806':
     coffee(id1)
   else:
       print("try again")

elif id1 == 'Heet':
   password = getpass("~~ Password ~~\n")
   if password == '2807':
     coffee(id1)
   else:
       print("try again")

else:
    print("try again")






