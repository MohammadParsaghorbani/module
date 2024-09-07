encrypt_result = []
def code_1(text,way):
    encrypt = ""
    if way == 1:
        for i in text:
            aski = ord(i)*2-4
            encrypt += chr(aski)
        print(encrypt)
    elif way == 2:
        for i in text:    
            aski = ord(i)*2-8
            encrypt += chr(aski)
        print(encrypt)
    encrypt_result.append(encrypt)