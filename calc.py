import sys
op = sys.argv[1]
num1 = sys.argv[2]
num2 = sys.argv[3]
element = sys.argv[4]


def dectodec(number):

    pc = 0
    dummy = 0

    myn = list(number)
    myn2 = []
    for i in myn:
        if i.isalpha():
            return "Error letter in dectodec"
        if i.isdigit():
            if int(i) >= 0 and int(i) <= 9:
                myn2.append(i)
                pc +=1
        else:
            return "Error malformed in dectodec"
    decnum = "".join(myn2)
    realdecnum = int(decnum)
    return realdecnum
    

def bintodec(number):

    pc = 0
    dummy = 0

    myn = list(number)
    myn.reverse()
    for i in myn:
        if i.isalpha():
            return "Error letter in bintodec"
        if i.isdigit():
            if int(i) == 0 or int(i) == 1:
                dummy += int(i)*(2 ** pc)
                pc += 1
            else:
                return "Error incorrect number in bintodec"
        else:
            return "Error malformed in bintodec"
    return(dummy)
    
def octtodec(number):

    pc = 0
    dummy = 0

    myn = list(number)
    myn.reverse()
    for i in myn:
        if i.isalpha():
            return "Error letter in octtodec"
        if i.isdigit():
            if int(i) >= 0 and int(i) <= 7:
                dummy += int(i)*(8 ** pc)
                pc += 1
            else:
                return "Error incorrect number in octtodec"
        else:
            return "Error malformed in octtodec"
    return(dummy)
    
def hextodec(number):

    pc = 0
    dummy = 0

    myn = list(number)
    myn.reverse()
    for i in myn:
        if i == "a" or i == "A":
            num = 10
            dummy += num*(16 ** pc)
            pc += 1
        elif i == "b" or i == "B":
            num = 11
            dummy += num*(16 ** pc)
            pc += 1
        elif i == "c" or i == "C":
            num = 12
            dummy += num*(16 ** pc)
            pc += 1
        elif i == "d" or i == "D":
            num = 13
            dummy += num*(16 ** pc)
            pc += 1
        elif i == "e" or i == "E":
            num = 14
            dummy += num*(16 ** pc)
            pc += 1
        elif i == "f" or i == "F":
            num = 15
            dummy += num*(16 ** pc)
            pc += 1
        elif i.isalpha():
            return "Error incorrect letter in hextodec"
        elif i.isdigit():
            if int(i) >= 0 and int(i) <= 9: 
                dummy += int(i)*(16 ** pc)
                pc += 1
            else:
                return "Error incorrect number in hextodec"
        else:
            return "Error malformed in hextodec"
    return(dummy)



def dectobin(a): #Number is a dec that you will convert to binary
    
    b = 0
    l = []

    while(a != 0):
        b = a%2
        a = a//2
        l.append(b)
    l.reverse()
    str1 = "".join(str(b) for b in l)
    final = "B"+str1
    return final


def dectooct(a): #Number is a dec that you will convert to octal
    
    b = 0
    l = []

    while(a != 0):
        b = a%8
        a = a//8
        l.append(b)
    l.reverse()
    str1 = "".join(str(b) for b in l)
    final = "O"+str1
    return final

def dectohex(a): #Number is a dec that you will convert to hex
    
    b = 0
    l = []

    while(a != 0):
        b = a%16
        a = a//16
        if b == 10:
            b = "A"
        elif b == 11:
            b = "B"
        elif b == 12:
            b = "C"
        elif b == 13:
            b = "D"
        elif b == 14:
            b = "E"
        elif b == 15:
            b = "F"

        l.append(b)
    l.reverse()
    str1 = "".join(str(b) for b in l)
    final = "X"+str1
    return final
        
def calc(op, num1, num2, element):

    x = num1
    y = num2
    fb = 0
    fb2 = 0
    finalfb = 0

    if x == "" or x == " ":
        return "Error no input for num1"
    if y == "" or y == " ":
        return "Error no input for num2"

    if x[0] == "-":
        if len(x) <= 1 or x[1] == " ":
            return "Error no input after negative num1 1"
        if x[1] == "b" or x[1] == "B":
            if len(x) <= 2 or x[2] == " ":
                return "Error no input type b num1 2"
            else:
                apples = (bintodec(x[2:]) * -1)
        if x[1] == "o" or x[1] == "O":
            if len(x) <= 2 or x[2] == " ":
                return "Error no input type o num1 3"
            else:
                apples = (octtodec(x[2:]) * -1)
        if x[1] == "x" or x[1] == "X":
            if len(x) <= 2 or x[2] == " ":
                return "Error no input type x num1 4"
            else:
                apples = (hextodec(x[2:]) * -1)
        if x[1] == "d" or x[1] == "D":
            if len(x) <= 2 or x[2] == " ":
                return "Error no input type d num1 5"
            else:
                apples = (dectodec(x[2:]) * -1)
        if x[1] != "b" and x[1] != "B" and x[1] != "o" and x[1] != "O" and x[1] != "x" and x[1] != "X" and x[1] != "d" and x[1] != "D":
            return "Error invalid number type for negative num1 6"

    if y[0] == "-":
        if len(y) <= 1 or y[1] == " ":
            return "Error no input after negative num2 7"
        if y[1] == "b" or y[1] == "B":
            if len(y) <= 2 or y[2] == " ":
                return "Error no input type b num2 8"
            else:
                oranges = (bintodec(y[2:]) * -1)
        if y[1] == "o" or y[1] == "O":
            if len(y) <= 2 or y[2] == " ":
                return "Error no input type o num2 9"
            else:
                oranges = (octtodec(y[2:]) * -1)
        if y[1] == "x" or y[1] == "X":
            if len(y) <= 2 or y[2] == " ":
                return "Error no input type x num2 10"
            else:
                oranges = (hextodec(y[2:]) * -1)
        if y[1] == "d" or y[1] == "D":
            if len(y) <= 2 or y[2] == " ":
                return "Error no input type d num2 11"
            else:
                oranges = (dectodec(y[2:]) * -1)
        if y[1] != "b" and y[1] != "B" and y[1] != "o" and y[1] != "O" and y[1] != "x" and y[1] != "X" and y[1] != "d" and y[1] != "D":
            return "Error invalid number type for negative num2 12."


   
    if x[0] != "-":
        if len(x) <= 1 or x[0] == " ":
            return "Error no input num1 13"
        if x[0] == "b" or x[0] == "B":
            if len(x) <= 1 or x[1] == " ":
                return "Error no input type b num1 14"
            else:
                apples = bintodec(x[1:])
        if x[0] == "o" or x[0] == "O":
            if len(x) <= 1 or x[1] == " ":
                return "Error no input type o num1 15"
            else:
                apples = octtodec(x[1:])
        if x[0] == "x" or x[0] == "X":
            if len(x) <= 1 or x[1] == " ":
                return "Error no input type x num1 16"
            else:
                apples = hextodec(x[1:])
        if x[0] == "d" or x[0] == "D":
            if len(x) <= 1 or x[1] == " ":
                return "Error no input type d num1 17"
            else:
                apples = dectodec(x[1:])
        if x[0] != "b" and x[0] != "B" and x[0] != "o" and x[0] != "O" and x[0] != "x" and x[0] != "X" and x[0] != "d" and x[0] != "D":
            return "Error invalid number type for num1 18"


    if y[0] != "-":
        if len(y) <= 1 or y[0] == " ":
            return "Error no input num2 19"
        if y[0] == "b" or y[0] == "B":
            if len(y) <= 1 or y[1] == " ":
                return "Error no input type b num2 20"
            else:
                oranges = bintodec(y[1:])
        if y[0] == "o" or y[0] == "O":
            if len(y) <= 1 or y[1] == " ":
                return "Error no input type o num2 21 "
            else:
                oranges = octtodec(y[1:])
        if y[0] == "x" or y[0] == "X":
            if len(y) <= 1 or y[1] == " ":
                return "Error no input type x num2 22"
            else:
                oranges = hextodec(y[1:])
        if y[0] == "d" or y[0] == "D":
            if len(y) <= 1 or y[1] == " ":
                return "Error no input type d num2 23"
            else:
                oranges = dectodec(y[1:])
        if y[0] != "b" and y[0] != "B" and y[0] != "o" and y[0] != "O" and y[0] != "x" and y[0] != "X" and y[0] != "d" and y[0] != "D":
            return "Error invalid number type for num2 24"



    if type(apples) is str or type(oranges) is str:
        return "Error malformed in num1 or num2"
    if op == "+":
        fb = apples + oranges
    elif op == "-":
        fb = apples - oranges
    elif op == "m":
        fb = (apples * oranges)
    else:
        return "Error: not valid operations"

    valid = False
    fb3 = str(fb)
    if fb3[0] == '-':
        fb2 = fb * -1
        valid = True


    if valid == False:
        if element == "d" or element == "D":
            finalfb = "D" + str(fb)
            return finalfb
        if element == "b" or element == "B":
            finalfb = dectobin(fb)
            return finalfb
        if element == "o" or element == "O":
            finalfb = dectooct(fb)
            return finalfb
        if element == "x" or element == "X":
            finalfb = dectohex(fb)
            return finalfb
        else:
            return "Error: elements not valid"

    if valid == True:
        if element == "d" or element == "D":
            finalfb = "D" + str(fb2)
            return "-" + finalfb
        if element == "b" or element == "B":
            finalfb = dectobin(fb2)
            return "-" + finalfb
        if element == "o" or element == "O":
            finalfb = dectooct(fb2)
            return "-" + finalfb
        if element == "x" or element == "X":
            finalfb = dectohex(fb2)
            return "-" + finalfb
        else:
            return "Error: elements not valid"


print(calc(op, num1, num2, element))
