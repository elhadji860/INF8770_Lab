import huffman_compress

class Dictionary : 
    size = 0
    container = []
    
    def __init__(self, size):
        self.size = size

    def clearDict(self): 
        self.container.clear()
    
    def addElement(self, element) : 
        self.container = [element] + self.container
    
    def matchingIndexes(self, element) : 
        indices = []

        for i, x in enumerate(self.container):
            if x == element:
                indices.append(i)

        return indices
    

def compress(txt, dictSize) : 

    compressionInfo = []    
    
    i = 0
    dictionary = Dictionary(dictSize)


    while (i < len(txt) - 1) : 
        
        # remplir le dictionnaire
        filling_index = 1
        dictionary.clearDict()
        while filling_index < 5 and i - filling_index > 0 : 
            dictionary.addElement(txt[i - filling_index])
            filling_index += 1
        
        matchingIndexes = dictionary.matchingIndexes(txt[i])
        matchingLength = 0
        chosenX = 0


        for x in matchingIndexes : 
            matchingIndexes = 1
            first_index = i - x
            second_index = i + 1

            temp_matching_length =1

            while ((txt[first_index] == txt[second_index]) and ((second_index) < len(txt) - 1)) : 
                temp_matching_length += 1
                first_index += 1
                second_index += 1
                

            if(temp_matching_length >= matchingLength):
                matchingLength = temp_matching_length
                chosenX = x

        i += matchingLength + 1

        if(matchingLength == 0) : 
             compressionInfo.append([0 , 0, txt[i - 1]])
        else : 
            compressionInfo.append([chosenX + 1 , matchingLength, txt[i - 1]])
        
    compressedString = ""

    for x in compressionInfo : 
        compressedString += str(x[0])
        compressedString += str(x[1])
        compressedString += str(x[2])

    print(compressedString)
    
    return huffman_compress.compress(compressedString)

   

    