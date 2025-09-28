from fractions import Fraction
import math
import huffman_compress

class Interval() : 
    maxLimit= 1
    minLimit = 0
    deltaLimit = 1

    singularIntervals = []
    charProb = []

    def changeLimits(self, minLimit, maxLimit) : 
        self.maxLimit = maxLimit
        self.minLimit = minLimit
        self.deltaLimit = maxLimit - minLimit

    def registerChar(self, char, prob) : 
        self.charProb.append((char, prob))

    def defineSingIntervals(self) : 
        self.singularIntervals.clear()
        position = self.minLimit

        for x in self.charProb : 
            self.singularIntervals.append((x[0], position, position + self.deltaLimit * x[1]))
            position += self.deltaLimit * x[1]


def shortest_binary_fraction_in_interval(a: float, b: float):

    if a > b:
      return

    q = 0
    while True:
        denom = 2 ** q
        p_min = math.ceil(a * denom)
        p_max = math.floor(b * denom)
        
        if p_min <= p_max: 
            frac = Fraction(p_min, denom)
            return fraction_to_binary(frac)
        
        q += 1  

def fraction_to_binary(frac: Fraction) -> str:
    p, q = frac.numerator, frac.denominator

    integer_part = p // q
    result = bin(integer_part)[2:]  
    remainder = p % q
    
    if remainder == 0:
        return result 
    
    result += "."
    while remainder > 0:
        remainder *= 2
        bit = remainder // q
        result += str(bit)
        remainder %= q
    return result


def compress(txt) : 
    interval = Interval()

    data = {}

    for char in txt :
        if(data.get(char)) :
            data[char] += 1
        else : 
            data.setdefault(char, 1)
    
    amountOfChar = 0

    for key in data : 
        amountOfChar += data[key]

    for key in data : 
        interval.registerChar(key, data[key]/amountOfChar)
    
    interval.defineSingIntervals()


    for x in txt : 
        limits = []
        for tuple in interval.singularIntervals : 
            if tuple[0] == x : 
                limits.append(tuple[1])
                limits.append(tuple[2])
        interval.changeLimits(limits[0], limits[1])

        interval.defineSingIntervals()
        
    frequencies_string = ""
    
    for key in data : 
        frequencies_string += key
        frequencies_string += str(data[key])

    
    return huffman_compress.compress(frequencies_string) + shortest_binary_fraction_in_interval(interval.minLimit, interval.maxLimit) + huffman_compress.compress(str(len(txt)))

    