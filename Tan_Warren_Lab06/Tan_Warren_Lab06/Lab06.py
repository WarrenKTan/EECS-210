# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 06
# Description: produces an output the next permutation in lexicographic order
# Collaborators: None

def main():
    # test inputs
    # inputNum = "230415"
    # inputNum = "671954"
    # inputNum = "4218753"
    inputList = ["45312", "13245", "612345", "1623547", "23587416"]

    # get userInputs
    # inputNum = input("Enter an integer: ")
    # inputList = [inputNum]
    
    for inputNum in inputList:
        # find pivot index
        pivotIndex = pivot(inputNum)
        prefix = inputNum[:pivotIndex]
        pivotPoint = inputNum[pivotIndex]
        suffix = inputNum[(pivotIndex + 1):]

        # find right successor
        rightSuccessor = successor(suffix, int(inputNum[pivotIndex]))

        # swap the pivot and right successor
        swappedPivot = swap(pivotPoint + suffix, 0, rightSuccessor + 1)

        reversedPivot = swappedPivot[0]

        # remove first index of swappedPivot
        swappedPivot = swappedPivot[1:]
        
        # reverses suffix
        reversedPivot += swappedPivot[::-1]

        print(f"inputNum: {inputNum}, outputNum: {prefix + reversedPivot}")

# finds longest non-increasing suffix
def pivot(inputNum):
    for i, left in enumerate(inputNum[-2::-1]):
        right = inputNum[(i*-1) - 1]
        if int(left) < int(right):
            return len(inputNum) + (i*-1) - 2
        elif int(left) == int(right):
            raise ValueError("The input must only contain unique numbers.")

# find the right-most successor in suffix
def successor(suffix, pivotNum: int):
    for i, num in enumerate(suffix[1:]):
        if int(num) < pivotNum:
            return i
    return len(suffix) - 1

# swaps index1 and index2 and returns the resulting string
def swap(inputNum, index1, index2):
    lst = list(inputNum)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return "".join(lst)

if __name__ == "__main__":
    main()