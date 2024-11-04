# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 09
# Description: computes transitive closure using Warshall's algorithm
# Collaborators: None

def main():
    # example formatting
    print("\nformat: \n\"1 2 3, 4 5 6, 7 8 9\"")
    printArr([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # userInput = input("Enter the array: ")
    # print()

    # test cases
    # userInput = "1 0 1, 0 1 0, 1 1 0"
    userInput = "0 0 0 1, 1 0 1 0, 1 0 0 1, 0 0 1 0"
    
    # takes string, returns integer array
    processed = processInput(userInput)

    print("input:")
    printArr(processed)

    print("output:")
    printArr(transitive_closure(processed))



def transitive_closure(arrM):
    n = len(arrM)
    for _ in range(2, n):
        arrM = warshall(arrM)
    return arrM

def warshall(arrM):
    n = len(arrM)
    arrW = arrM
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # no connection, and has a transitive connection
                hasConneciton = (arrW[i][j] != 1) and (arrW[i][k] == 1) and (arrW[k][j] == 1)
                alreadyConnected = (arrW[i][j] == 1)
                if hasConneciton or alreadyConnected:
                    arrW[i][j] = 1
                else:
                    arrW[i][j] = 0

    return arrW
                
                        
                

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