# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 04
# Description: implements the merging of two ordered lists
# Collaborators: None

def main():
    # get userInputs
    inputList1 = input("Enter list #1: ")
    inputList2 = input("Enter list #2: ")
    
    # test inputs
    # inputList1 = "4, 7, 17, 22, 85"
    # inputList2 = "5, 11, 14, 19, 108, 210, 747"
    # inputList1 = "5, 17, 85, 108, 210"
    # inputList2 = "4, 7, 17, 22, 85"
    
    # convert inputs to lists
    list1 = toList(inputList1)
    list2 = toList(inputList2)

    # merge lists together
    merged = merge(list1, list2)

    # print merged lists
    for i, j in enumerate(merged):
        if (i != (len(merged) - 1)):
            print(j, end=", ")
        else:
            print(j)

# converts input from a string to list
def toList(textList):
    returnList = textList.split(",")
    for i, _ in enumerate(returnList):
        returnList[i] = int(returnList[i].strip(" "))
    return returnList

# merge lists together
def merge(list1, list2):
    returnList = []

    while(len(list1) > 0 and len(list2) > 0):
        firstVal1 = list1[0]
        firstVal2 = list2[0]
        if firstVal1 < firstVal2: # remove 1 if 1<2
            returnList.append(list1.pop(0))
        elif (firstVal2 < firstVal1): # remove 2 if 2<1
            returnList.append(list2.pop(0))
        else: # remove both and append one of the values
            returnList.append(list2.pop(0))
            list1.pop(0)

    returnList = returnList + list2 + list1

    return returnList

if __name__ == "__main__":
    main()