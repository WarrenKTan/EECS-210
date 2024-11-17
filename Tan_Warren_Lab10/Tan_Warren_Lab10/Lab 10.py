# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 10
# Description: 
# Collaborators: None

def main():

    # example formatting
    exampleInput = "1 2 3, 4 5 6, 7 8 9"
    print(f"\nformat: \n\"{exampleInput}\"")
    printArr(processInput(exampleInput))

    userInput = input("Enter the array: ")
    print()

    # test cases
    # userInput = "0 1 0 1, 1 0 1 0, 0 1 0 1, 1 0 1 0"
    
    # takes string, returns integer array
    processed = processInput(userInput)

    print("input:")
    printArr(processed)

    print("output:")
    eulerPath = euler(processed)
    printArr(convertLetters(eulerPath))
    print()



def euler(arrG : list):
    # start from any point because each vertex has an even number of edges
    stack = [0]
    stack[-1]
    circuit = []

    # while arrG has edges (1s)
    while stack:
        prevNode = stack[-1]
        edgeFound = False
        
        # attempt to find subcircuits
        for curNode, edge in enumerate(arrG[prevNode]):
            # edge is found
            if edge == 1:
                stack.append(curNode)
                arrG = removeEdge(arrG, prevNode, curNode)
                edgeFound = True
                break
        
        # no more subcircuits to be found
        if not edgeFound:
            circuit.append(stack.pop())

    return reversed(circuit)

# remove edge between i and j from arrH
def removeEdge(arrH : list, i : int, j : int):
    arr = arrH
    if (arr[i][j] == 1) and (arr[j][i] == 1):
        arr[i][j] = 0
        arr[j][i] = 0
    else:
        print("uhhh some logic is wrong")
    return arr



# prints array as shown
def printArr(arr : list):
    returnStr = ""
    for _, var in enumerate(arr):
        if type(var) is list:
            printArr(var)
        else:
            print(var, end=" ")
            returnStr = returnStr + str(var) + " "
    print()
    return returnStr

# converts the example input to array that is returned
def processInput(userInput):
    # splits array into 1d array with strings
    stringArr = userInput.strip().split(",")
    stringArr2 = []
    for _, j in enumerate(stringArr):
        stringArr2.append(j.strip().split(" "))

    # converts string to integer array
    arr = [list(map(int,i)) for i in stringArr2]
    return arr

# converts 1D number array to letters (0 -> a, 1 -> b, etc.) and returns the result
def convertLetters(numArr : list):
    letArr = []
    for num in numArr:
        letArr.append(chr(ord('a') + num))
    
    return letArr

if __name__ == "__main__":
    main()