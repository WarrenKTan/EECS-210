# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 03
# Description: implements the fast modular exponentiation based on the binary expansion of the exponent
# Collaborators: None

def main():
    # get userInputs
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent (base 10): "))
    modulus = int(input("Enter the modulus: "))

    # parse exponent to list of its binary bits
    binaryExponent = toBinary(int(exponent))
    
    # limits maximum amount of values in binaryTable
    bitAmount = len(binaryExponent)
    
    # binary table of modulated bits
    # ex: 
    # base = 5
    # modulus = 19
    # binaryTable[0] = 5 % 19 = 5
    # binaryTable[1] = (binaryTable[0]**2) % 19 = 6
    # etc.
    binaryTable = binaryModTable(base, bitAmount, modulus)

    # multiplies end-products
    reducedNumList = []
    if len(binaryTable) == len(binaryExponent):
        for i, _ in enumerate(binaryExponent):
            match binaryExponent[i]:
                case 1:
                    reducedNumList.append(binaryTable[i])
                case 0:
                    pass

    # multiplies list together to get the final reduced num
    reducedNum = reducedNumList[0]
    for i, _ in enumerate(reducedNumList):
        if i != 0:
            reducedNum *= reducedNumList[i]

    print(f"{base}^{exponent} % {modulus} = {reducedNum % modulus}", end="\n\n")
                    
                    

# parses input into a list of its binary values
def toBinary(inputVal: int):
    # convert value to binary string
    outputVal = bin(inputVal)[2:]

    # create list to return
    outputList = []
    for i in reversed(outputVal):
        outputList.append(int(i))
        pass
    
    return outputList
    pass

# returns list of all modulated exponnents
def binaryModTable(base, maxBitAmount: int, modulus):
    bitCounter = 0
    outputList = []

    while bitCounter < maxBitAmount:
        if bitCounter == 0: # base modulus
            outputList.append(base % modulus)
        else: # uses previous modulus to make next value
            prevNum = outputList[-1]
            outputList.append(prevNum**2 % modulus)
        bitCounter += 1
    
    return outputList
    pass

if __name__ == "__main__":
    while True:
        main()