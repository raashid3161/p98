def swapFileData():
    userInput = input("Name a file ")
    userInput2 = input("Name second file ")
    with open(userInput, 'r') as a:
        dataA = a.read()
    with open(userInput2, 'r') as a:
        dataB = a.read()
    with open(userInput, 'w') as a:
        a.write(dataB)
    with open(userInput2, 'w') as a:
        a.write(dataA)
    print("successfully swapped")

swapFileData()