# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 11
# Description: implementation of dijkstra's algorithm
# Collaborators: Kevin Fan

def main():

    # example formatting
    # ~ is infinity because there's no infinity symbol ;-;
    exampleInput = "1 2 3, 4 ~ 6, 7 8 9"
    print(f"\nFormat: \n\"{exampleInput}\" (\"~\" = infinity)")
    printArr(processInput(exampleInput))

    userInput = input("Enter the array: ")
    print()
    vertex1 = input("Enter the starting vertex: ")
    print()
    vertex2 = input("Enter the ending vertex: ")
    print()

    # test case
    # userInput = "~ 6 3 ~, 6 ~ 4 1, 3 4 ~ 1, ~ 1 1 ~"
    # vertex1 = "b"
    # vertex2 = "a"
    
    # takes string, returns integer array
    processed = processInput(userInput)

    print("Input:")
    printArr(processed)
    print(f"Start: {vertex1}\nEnd:   {vertex2}\n")

    print("Output:")
    output = dijkstra(processed, vertex1, vertex2)
    printArr(convertLetters(output[0]), "Minimum Path:     ")
    print(f"Minimum Distance: {output[1]}")
    print()


# dijkstra's algorithm to find the shortest pathway between startChar and endChar
# outputs: path (list of indicies in order), distance
def dijkstra(arr : list, startChar : str, endChar : str):
    n = len(arr)
    dist = [None] * n
    prev = [float('inf')] * n
    unchecked = [i for i in range(n)]

    # convert inputs to integers
    start = ord(startChar) - ord('a')
    end = ord(endChar) - ord('a')

    # set starting distance to 0 (distance from 'a'->'a' is 0)
    dist[start] = 0

    # while there are unchecked verticies
    while unchecked:
        # find minVal in the unchecked verticies
        minIndex, minVal = minInIndicies(dist, unchecked)

        # print running variables for debugging
        # printArr(dist, "dist:      ")
        # print(f"minIndex:  {minIndex}")
        # print(f"minVal:    {minVal}")
        # printArr(unchecked, "unchecked: ")
        # printArr(prev, "prev:      ")
        # print()

        # remove minVal from the unchecked verticies
        unchecked.remove(minIndex)

        for vertex in unchecked:
            # currentDistance from start
            curDist = dist[minIndex]
            # distance to next point
            nextDist = arr[minIndex][vertex]

            # check if vertex exists
            if nextDist == "~":
                pass
            else:
                # create alternate path going towards each new vertex
                alt = curDist + nextDist
                if dist[vertex] is None or alt < dist[vertex]:
                    # update distance and previous travelled vertex
                    dist[vertex] = alt
                    prev[vertex] = minIndex 

    # dijkstra algorithm finished


    # processOutputs
    path = [end]
    curPos = end
    while prev[curPos] != float('inf'):
        path.insert(0, prev[curPos])
        curPos = prev[curPos]

    return path, dist[end]


# returns minimum index and value within definied indexes
def minInIndicies(keys : list, indicies : list):
    # first value from indicies
    index = indicies[0]
    min = keys[indicies[0]]
    for i in indicies:
        if keys[i] is None:
            pass
        elif min is None or keys[i] < min:
            index = i
            min = keys[i]
    return index, min
        


# prints array with spaces between indicies
def printArr(arr : list, preArr : str = ""):
    print(preArr, end="")
    for _, var in enumerate(arr):
        if type(var) is list:
            printArr(var)
        else:
            print(var, end=" ")
    print()

# converts the example input to array that is returned
def processInput(userInput : str):
    # splits array into 1d array with strings
    stringArr = userInput.strip().split(",")
    stringArr2 = []
    # splits subarrays into arrays
    for _, j in enumerate(stringArr):
        stringArr2.append(j.strip().split(" "))

    # converts string to integer & infinity array
    arr = []
    for charArr in stringArr2:
        subArr = []
        for char in charArr:
            try: # test for int
                subArr.append(int(char))
            except: # 'char' is not an integer
                subArr.append("~")
        arr.append(subArr)
    return arr

# converts 1D number array to letters (0 -> a, 1 -> b, ..., 26 -> z) and returns it
def convertLetters(numArr : list):
    letArr = []
    for num in numArr:
        letArr.append(chr(ord('a') + num))
    return letArr

if __name__ == "__main__":
    main()