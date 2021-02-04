import re

def checkReg(strReg):
    n = len(strReg)
    string = strReg.lower()
    if n == 6:
        if 'q' in string or 'i' in string or 'v' in string:
            print('False')
        else:
            x = string[0:3]
            y = string[3:5]
            z = string[5:]
            if x.isalpha() and y.isdigit():
                if z.isdigit() or z.isalpha():
                    print('True')
            else:
                print('False')
    else:
        print('False')
checkReg('1bc36')