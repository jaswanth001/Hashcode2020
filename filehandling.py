def process(fileName):

    # Print data to console
    print("")
    print("-----------------------")
    print(fileName)
    print("-----------------------")

    #  Read the open file by name
    inputFile = open(inputFilesDirectory + fileName + ".in", "rt")

    #  Read file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()


    #  Print input data
    print("INPUT")
    print(firstLine)
    print(secondLine)

    #  Assign parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)  # Solve the problem and get output

    #  Print output data and create output file
       
    print("")
    print("OUTPUT")
    print(len(outputList))

    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()

def solve(MAX, inputList):
    inputList = 'Add input'
    return 1
inputFilesDirectory = "Input/"  # Location of input files
outputFilesDirectory = "Output/"  # Location of output files

fileNames = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  # File names

for fileName in fileNames:  # Take each and every file and solve
    process(fileName)