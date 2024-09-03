def code_1(text,way):
    if way == 1:
        encrypt = ""
        for i in text:
            aski = ord(i)*2-4
            encrypt += chr(aski)
        print(encrypt)
    elif way == 2:
        encrypt = ""
        for i in text:    
            aski = ord(i)*3-7
            encrypt += chr(aski)