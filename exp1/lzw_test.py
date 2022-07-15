
import sys


# ========================================
# test cases:
# python3 lzw.py abrakadabra
# python3 lzw.py cabracadabrarrarrad
# python3 lzw.py mississipi
# ========================================

def longest_common_substring(s1, s2):
    # go along the first string and search for the longest match
    maxLongest = 0
    offset = 0
    for i in range(0, len(s1)):
        longest = 0
        if ((i == len(s1) - len(s2) - 2)):
            break
        for j in range(0, len(s2)):
            if (i + j < len(s1)):
                if s1[i + j] == s2[j]:
                    longest = longest + 1
                    if (maxLongest < longest):
                        maxLongest = longest
                        offset = i
                else:
                    break
            else:
                break
    return maxLongest, offset


def encode_lzw(text):
    dictionary = dict()
    # prepare the dictionary with the starting alphabet
    i = 0
    index = 1
    while i < len(text):
        if text[i] in dictionary:
            i = i + 1
        else:
            dictionary[text[i]] = index
            index = index + 1

    # encode the text
    i = 0
    encoded = []
    while i < len(text):
        j = 0
        stringToBeSaved = text[i]
        # while the stringToBeSaved is in the dictionary and we are not in the end of the string
        while stringToBeSaved in dictionary and i + j < len(text):
            # save longest dictionary occurence's index
            indexInDictionary = dictionary[stringToBeSaved]
            length = len(stringToBeSaved)
            if (i + j == len(text) - 1):
                break
            j = j + 1
            stringToBeSaved = stringToBeSaved + text[i + j]
        i = i + length
        # print ("<{0}>".format(indexInDictionary))
        encoded.append(indexInDictionary)
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
        index = index + 1

    return encoded, dictionary


def decode_lzw(encoded, dictionary):
    i = 0
    while i < len(encoded):
        print(list(dictionary.keys())[list(dictionary.values()).index(encoded[i])], end="")
        i = i + 1
    print('\n')


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        exit("You must specify the text which will be encoded! (Run with python3 lz77.py abracadabra)")
    stringToEncode = ' '.join(sys.argv[1:2])
    [encoded, dictionary] = encode_lzw(stringToEncode)
    print("Encoded string: ", encoded)
    print("Decoded string: ", end="")
    decode_lzw(encoded, dictionary)
