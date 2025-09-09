import math
import string

def initDictionary(str) : 
    data = {}
    count = 0

    for char in str :
        if( not char in data) :
            data.setdefault(char, count)
            count += 1

    return data 

def binary_to_ascii_with_replacement(binary_str, replacement='�'):
    binary_str = binary_str.replace(" ", "")
    binary_str = binary_str[:len(binary_str) - (len(binary_str) % 8)]

    result = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        char = chr(int(byte, 2))
        if char in string.printable and char not in '\t\n\r\x0b\x0c':
            result.append(char)
        else:
            result.append(replacement)
    return ''.join(result)


def compress(string) :
    
    dictionary = initDictionary(string)
    nbBit = math.ceil(math.log(len(dictionary), 2))

    compressedStringBit = ""
    i = 0

    while(i < len(string)) :
        j = i + 1
        
        while ((string[i:j] in  dictionary) & (j <= len(string))):
            
            j += 1
        
        count =  len(dictionary)
        dictionary.setdefault(string[i:j], count)

        nbBit = math.ceil(math.log(len(dictionary), 2))

        compressedStringBit +=  bin(((dictionary[string[i : j-1]])))[2:].zfill(8)

        i = j-1

    

    return binary_to_ascii_with_replacement(compressedStringBit)

print(compress("kikkoll"))
