from encrypt import encrypt_result , code_1
from decrypt import decrypt_result , code_2
# def info(choice,way,text,result):
#     with open("module_aski.txt" , "a") as file:
#         file.write(f"***************\nchoice = {choice}\nway = {way}\ntext = {text}\nresult = {result}\n")
file = open("module_aski.txt" , "a")
while True :
    choice = int(input("options:\n\t 1)encrypt\n\t 2)decrypt\n\t 3)exit\n"))
    if choice == 1:
        text = input("enter your text: ")
        way = int(input("we have two way for encrypt,which one? "))
        code_1(text,way)
        # info(choice,way,text,encrypt_result)
    elif choice == 2:
        text = input("enter your text: ")
        way = int(input("we have two way for encrypt,which one? "))
        code_2(text,way)
        # info(choice,way,text,decrypt_result)
    elif choice == 3:
        print("good bye!")
        break
    else:
        print("wrong option!")
file.close()
#finish