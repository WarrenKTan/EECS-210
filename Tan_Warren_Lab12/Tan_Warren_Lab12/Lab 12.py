# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 12
# Description: 
# Collaborators: 

def main():

    exampleInput = "^ - x y 2"
    print("\nuse space (' ') to separate individual components")
    print(f"Format: \n\"{exampleInput}\"\n")

    userInput = input("Enter the expression: ")
    print()

    # test case
    # userInput = "^ - x y 2"

    # userInput = "/ - x y * y z"

    # userInput = "+ ^ - x 2 2 ^ - y 1 3"
    
    # takes string, returns integer array
    processed = processInput(userInput)

    print("Prefix:")
    printArr(processed)
    print()

    infix = preToIn(processed)

    print("Infix:")
    printArr(infix)
    print()

    postfix = inToPost(infix)

    print("Postfix:")
    printArr(postfix)
    print()


# converts a prefix expression to infix
def preToIn(prefix : list):
    stack = []
    operations = ["+", "-", "*", "/", "^"]

    for i in reversed(prefix):
        
        if i not in operations: # number or variable
            stack.append(i)
        
        else:
            if(len(stack) > 1):
                # find previous 2 numbers
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)

                # combine val1 and val2 with the operation and parentheses surrounding
                newVal = f"( {val1} {i} {val2} )"
                

                stack.append(newVal)
            else:
                print("operator does not have enough values.")

    return processInput(stack[0])

# converts a infix expression to postfix
def inToPost(infix: list):
    output = []
    stack = []
    operations = ["+", "-", "*", "/", "^", "(", ")"]
    
    for i in infix:
        
        if i not in operations: # number or variable
            output.append(i)

        else:
            if(i == ")"):
                # backtrack stack until "("
                while stack[-1] != "(":
                    output.append(stack.pop(-1))
                    
                stack.pop(-1)

            else:
                # non-closing parentheses operation encountered
                stack.append(i)

    return output

# prints array with spaces between indicies
def printArr(arr : list, preArr : str = ""):
    print(preArr, end="")
    for _, var in enumerate(arr):
        if type(var) is list:
            printArr(var)
        else:
            print(var, end="")
    print()

# converts the example input to array that is returned
def processInput(userInput : str):
    # splits array into 1d array with strings
    stringArr = userInput.strip().split(" ")
    return stringArr

if __name__ == "__main__":
    main()