# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 07
# Description: 
# Collaborators: None

def main():
    # get userInputs
    inputNum = int(input("Enter an integer: "))

    getSequences("", inputNum, 1)
    pass

# returns all sequences 
def getSequences(curVal, maxLen, prevVal):
    if maxLen == len(curVal):
        print(curVal, end=", ")
        return 

    if prevVal == 0: # next value cannot be a 0
        getSequences(curVal + "1", maxLen, 1)
    else: # next value can be either 1 or 0
        getSequences(curVal + "0", maxLen, 0)
        getSequences(curVal + "1", maxLen, 1)

if __name__ == "__main__":
    main()