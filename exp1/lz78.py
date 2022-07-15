import sys


def encode(text):
    #传进字符串abracadabra
    mydict = dict()
    i = 0
    index = 1
    lstNumbers = []
    lstLetters = []

    # writing your code to encode text with LZ78
##########################################################################
    while i < len(text):
        stringToBeSaved = text[i]
        index = 0
        while stringToBeSaved in mydict:
            index = mydict[stringToBeSaved] # 找该字符在字典中的下标
            if (i == len(text) - 1):
                stringToBeSaved = " "
                break
            i = i + 1
            stringToBeSaved = stringToBeSaved + text[i]
            #print(stringToBeSaved)   ac   ad  ab  ra
        #print ("<{0}, {1}>".format(index, stringToBeSaved[len(stringToBeSaved) - 1]))
        lstNumbers.append(index)
        lstLetters.append(stringToBeSaved[len(stringToBeSaved) - 1]) # 加入最后一个字符
        if (stringToBeSaved not in mydict):
            mydict[stringToBeSaved] = index  #以（index，string）形式存入字典中
            index = index + 1
        i = i + 1
##########################################################################
    return lstNumbers, lstLetters, mydict


def decode(lstNumbers, lstLetters, mydict):
    i = 0
    while i < len(lstNumbers):
        if (lstNumbers[i] != 0):
            print(list(mydict.keys())[list(mydict.values()).index(lstNumbers[i])], end="")
        print(lstLetters[i], end="")
        i = i + 1
    print('\n')


if __name__ == "__main__":
    # if (len(sys.argv) != 2):
    #     exit("Usage:(Run with python lz78.py abracadabra)")
    # stringToEncode = ''.join(sys.argv[1:2])
    stringToEncode=input()
    [lstNumbers, lstLetters, mydict] = encode(stringToEncode)
    print("Encoded string: ", end="")
    i = 0
    while i < len(lstNumbers):
        print("<{0}, {1}>".format(lstNumbers[i], lstLetters[i]), end=" ")
        i = i + 1
    print('\n')
    print("Decoded string: ", end="")
    decode(lstNumbers, lstLetters, mydict)
