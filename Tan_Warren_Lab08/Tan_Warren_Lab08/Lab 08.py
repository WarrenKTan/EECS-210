# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 08
# Description: 
# Collaborators: None

def main():
    # userInput = int(input("Enter the array: "))

    # userInput = [[1, 0, 1], [0, 1, 0], [1, 1, 0]]
    userInput = [[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]

    print("input")
    printArr(userInput)

    print("output")
    printArr(transitive_closure(userInput))

    # arrA = arrM = userInput
    # for i in range(4):
    #     for j in range(4):
    #         print(valueAtPosition(i, j, arrA, arrM))



def transitive_closure(arrM):
    arrB = arrA = arrM
    n = len(arrM)
    for i in range(2, n + 1):
        arrA = boolMultiplication(arrA, arrM)
        print(f"arrA, iteration {i}")
        printArr(arrA)
        
        arrB = OR(arrB, arrA)
        print(f"arrB, iteration {i}")
        printArr(arrB)
    return arrB

# find next iteration of arrA
def boolMultiplication(arrA, arrM):
    newArr = arrA
    n = len(arrM)
    for i in range(n):
        for j in range(n):
            newArr[i][j] = valueAtPosition(i, j, arrA, arrM)

            # print(f"{i}, {j}")
            # printArr(arrA)
            # print(arrA[3][0])
    
    return newArr

# perform OR function on two arrays
def OR(arrB, arrA):
    for i, _ in enumerate(arrB):
        for j, _ in enumerate(arrB[i]):
            if arrB[i][j] == 1 or arrA[i][j] == 1:
                arrB[i][j] = 1
            else:
                arrB[i][j] = 0
    return arrB

def printArr(arr):
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i]):
            print(arr[i][j], end=" ")
        print()
    print()

def valueAtPosition(i, j, arrA, arrM):
    n = len(arrA[i])
    for k in range(n):
        if (arrA[i][k] == 1 and arrM[k][j] == 1):
            return 1
    return 0

if __name__ == "__main__":
    main()