# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 08
# Description: computes transitive closure
# Collaborators: None

def main():
    # example formatting
    print("format: \n\"1 2 3, 4 5 6, 7 8 9\"")
    printArr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    userInput = input("Enter the array: ")
    print()

    # test cases
    # userInput = "1 0 1, 0 1 0, 1 1 0"
    # userInput = "0 0 0 1, 1 0 1 0, 1 0 0 1, 0 0 1 0"
    
    # takes string, returns integer array
    processed = processInput(userInput)

    print("input:")
    printArr(processed)

    print("output:")
    printArr(transitive_closure(processed))



def transitive_closure(arrM):
    arrB = arrA = arrM
    n = len(arrM)
    for i in range(2, n + 1):
        arrA = boolMultiplication(arrA, arrM)
        arrB = OR(arrB, arrA)
    return arrB

# find next iteration of arrA
def boolMultiplication(arrA, arrM):
    n = len(arrM)
    returnArr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            returnArr[i][j] = valueAtPosition(i, j, arrA, arrM)
    
    return returnArr

# perform OR function on two arrays
def OR(arrB, arrA):
    for i, _ in enumerate(arrB):
        for j, _ in enumerate(arrB[i]):
            if arrB[i][j] == 1 or arrA[i][j] == 1:
                arrB[i][j] = 1
            else:
                arrB[i][j] = 0
    return arrB

# prints array as shown
def printArr(arr):
    returnStr = ""
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i]):
            print(arr[i][j], end=" ")
            returnStr = returnStr + str(arr[i][j]) + " "
        print()
    print()
    return returnStr

# gets value at position in next array
def valueAtPosition(i, j, arrA, arrM):
    n = len(arrA[i])
    for k in range(n):
        if (arrA[i][k] == 1 and arrM[k][j] == 1):
            return 1
    return 0

def processInput(userInput):
    # splits array into 1d array with strings
    stringArr = userInput.strip().split(",")
    stringArr2 = []
    for _, j in enumerate(stringArr):
        stringArr2.append(j.strip().split(" "))

    # converts string to integer array
    arr = [list( map(int,i) ) for i in stringArr2]
    return arr

if __name__ == "__main__":
    main()