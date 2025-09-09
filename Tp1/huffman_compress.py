import string
import sys

class HuffmanNode :
    left = None 
    right = None
    compressedCode = None
    weight = 0

    def __init__(self, leftNode = None, rightNode = None, weight = 0):
        self.left = leftNode
        self.right = rightNode
        self.weight = weight
    

    def setCompressedCode(self, newCompressedCode):
        self.compressedCode = newCompressedCode
    

class HuffmanTree :
    root = None

    def __init__(self, root = None):
        self.root = root

def generateNodes(charFreqDic) :
    charNodeDic = {}

    for key in charFreqDic:
        charNodeDic.setdefault(key, HuffmanNode(weight = charFreqDic[key]))

    return charNodeDic

def isolateNodes(charNodeDic) : 
    nodeList = []
    for key in charNodeDic :
        nodeList.append(charNodeDic[key])

    return nodeList

def buildTree(charNodeDic) : 
    nodeList = isolateNodes(charNodeDic)

    while(len(nodeList) > 1) :
        nodeList.sort(key=lambda x: x.weight)
        firstElement = nodeList.pop(0)
        secondElement = nodeList.pop(0)

        newNode = HuffmanNode(leftNode=firstElement, rightNode=secondElement, weight=firstElement.weight + secondElement.weight)
        nodeList.append(newNode)
    
    return HuffmanTree(root=nodeList[0])

def generateCompressedCode(node, addedCode) : 
    node.setCompressedCode(addedCode)

    if(node.left) : 
        generateCompressedCode(node.left, node.compressedCode + '1')
    if(node.right) :
        generateCompressedCode(node.right, node.compressedCode + '0')

def findWeight(str):
    data = {}

    for char in str :
        if(data.get(char)) :
            data[char] += 1
        else : 
            data.setdefault(char, 1)

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


def compress(str) : 
    data  = findWeight(str)

    dictNode = generateNodes(data)
    newTree = buildTree(dictNode)
    generateCompressedCode(newTree.root, "")

    compressedStrBit = ""
    for char in str : 
        compressedStrBit += dictNode[char].compressedCode

    compressedText = binary_to_ascii_with_replacement(compressedStrBit)

    #print (print(sys.getsizeof(str), "bytes \n"))
    #print (print(sys.getsizeof(compressedText), "bytes \n"))

    return compressedText



print(compress("dfdjfeofkofrnj"))
    

