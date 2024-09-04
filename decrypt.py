decrypt_result = []
def code_2(text,way):
    if way == 1:
        decrypt = ""
        for i in text:
            a = ord(i)+4
            a = a//2
            decrypt += chr(a)
        print(decrypt)
    elif way == 2:
        decrypt = ""
        for i in text:
            a = ord(i)+7
            a = a//3
            decrypt += chr(a)
        print(decrypt)
    decrypt_result.append(decrypt)