import sys

number = sys.argv[1]


def bintodec32(number):
    pc = 0
    dummy = 0

    myn = list(number)
    myn.reverse()
    for i in myn:
        if i.isdigit():
            if int(i) == 0 or int(i) == 1:
                dummy += int(i) * (2 ** pc)
                pc += 1
            else:
                return "Error incorrect number for positive bintodec"
        else:
            return "Error not valid binary"
    return (dummy)


def bintodec32neg(number):
    listneg = []

    for i in range(len(number)):
        if number[0] == "1":
            if number[i] != "1" and number[i] != "0":
                return "Error not valid character"
            if number[i] == "1":
                listneg.append("0")
            if number[i] == "0":
                listneg.append("1")
    x = "".join(listneg)
    lemon = bintodec32(x)
    lemon += 1
    return "-" + str(lemon)


def formatbd(number):
    if len(number) != 32:
        return "Error need more or less digits"
    if number[0] == "1":
        peaches = bintodec32neg(number)
        return peaches
    if number[0] == "0":
        pinapple = bintodec32(number)
        return pinapple
    else:
        return "Error not 0 or 1 check it again"


print(formatbd(number))
