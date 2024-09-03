from encrypt import *
from decrypt import *
file = open("module_aski.txt" , "a")
while True :
    choice = int(input("options:\n\t 1)encrypt\n\t 2)decrypt\n\t 3)exit\n"))
    if choice == 1:
        text = input("enter your text: ")
        way = int(input("we have two way for encrypt,which one? "))
        code_1(text,way)
    elif choice == 2:
        text = input("enter your text: ")
        way = int(input("we have two way for encrypt,which one? "))
        code_2(text,way)
    elif choice == 3:
        print("good bye!")
        break
    else:
        print("wrong option!")
file.close()
#finish