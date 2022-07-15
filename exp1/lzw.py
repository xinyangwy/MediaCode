import sys

def encode(text):

    mydict = dict()
    # prepare the initial mydict
##########################################################################
    i = 0
    index = 1
    while i < len(text):
        if text[i] in mydict:
            i = i + 1
        else:
            mydict[text[i]] = index
            index = index + 1

    # encode the text
    i = 0


    output = []
    # write your encoding code here...
##########################################################################
    while i < len(text):
        j = 0
        stringToBeSaved = text[i]
        # while the stringToBeSaved is in the mydict and we are not in the end of the string
        while stringToBeSaved in mydict and i + j < len(text):
            # save longest mydict occurence's index
            indexInDictionary = mydict[stringToBeSaved]
            length = len(stringToBeSaved)
            if (i + j == len(text) - 1):
                break
            j = j + 1
            stringToBeSaved = stringToBeSaved + text[i + j]
        i = i + length
        # print ("<{0}>".format(indexInDictionary))
        output.append(indexInDictionary)
        if (stringToBeSaved not in mydict):
            mydict[stringToBeSaved] = index
        index = index + 1
##########################################################################
    return output, mydict

def decode(output, mydict):
    i = 0
    while i < len(output):
        print(list(mydict.keys())[list(mydict.values()).index(output[i])], end="")
        i = i+1
    print('\n')


if __name__ == "__main__":
    # if (len(sys.argv) != 2):
    #     exit("Usage:(Run with python lzw.py abracadabra)")
    # input = ' '.join(sys.argv[1:2])
    text=input()
    [output, mydict] = encode(text)
    print("output string: ", output)
    print("Decoded string: ", end="")
    decode(output, mydict)
