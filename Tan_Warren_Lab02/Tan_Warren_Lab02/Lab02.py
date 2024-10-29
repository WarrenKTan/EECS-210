# Name: Warren Tan
# KUID: 3130842
# LAB Session: Tuesday 4 p.m.
# LAB Assignment: 02
# Description: take an input, produce output depending on function
# Collaborators: None

def main():
    # given example inputs
    # exampleInput = "(4, F) (5, G) (4, H)"
    # exampleInput = "(0,C) (3, G)"
    # exampleInput = "(0,C) (3, G) (2, A) (6, B) (4, D) (5, E) (7, F) (1, H)"

    userInput = input("input: ")

    myList = processInput(userInput)
    
    match isFunction(myList):
        case True:
            print("function", end="")
            
            if isOneToOne(myList):
                print(", one-to-one", end="")
                pass
            else:
                print(", not one-to-one", end="")

            if isOnto(myList):
                print(", onto", end="")
                pass 
            else:
                print(", not onto", end="")

            pass
        case False:
            print("not function")
            pass
    pass

# takes input, then maps it into an easily readable list
def processInput(input: str):
    myList = []

    individualInputs = input.strip("(").strip(")").split(") (")
    for pair in individualInputs:
        set_1_mapping = pair[0]
        set_2_mapping = pair[-1]
        myList.append((int(set_1_mapping), set_2_mapping))
        pass

    return myList
    pass

# returns 'True' if the pairs are functions
def isFunction(myList: list):
    # keeps track of elements from set 1 we've passed
    set_1_count = []
    
    for pair in myList:
        if pair[0] not in set_1_count:
            set_1_count.append(pair[0])
        else:
            return False
        pass

    return True
    pass

# returns 'True' if the pairs are one-to-one
def isOneToOne(myList: list):
    # keeps track of elements from set 2 we've passed
    set_2_count = []
    
    for pair in myList:
        if pair[1] not in set_2_count:
            set_2_count.append(pair[1])
        else:
            return False
        pass

    return True
    pass

# returns 'True' if the pairs are onto
def isOnto(myList: list):
    # keeps track of elements from set 2 we've passed
    set_2_count = []
    
    for pair in myList:
        if pair[1] not in set_2_count:
            set_2_count.append(pair[1])

    if len(set_2_count) >= 8:
        return True
    else:
        return False
    pass

if __name__ == "__main__":
    main()
    pass