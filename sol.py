file1 = "b_small"
inputFile = open(file1 + ".txt", "r")
line_num = 0

firstLine = inputFile.readline()
secondLine = inputFile.readline()
print("##")
BooksNo, LibNo, Day = list(map(int, firstLine.split()))

BookScore = list(map(int, secondLine.split()))
print("##")    
LibBookNo = [] 
SignUp = [] 
ShipLim  = []
BookIDCol = [ ] #book indexes in each lib
for l in range(LibNo):
    print("##")
    firstlibline = inputFile.readline()
    LibBook, Signs, Ships = list(map(int, firstlibline.split()))
    LibBookNo.append(LibBook)
    SignUp.append(Signs)
    ShipLim.append(Ships)
    secondlibline = inputFile.readline()
    
    BookID = list(map(int, secondlibline.split()))
    BookIDCol.append(BookID)
inputFile.close()

totalBookscore_perlib = [] 
#order of signUps
avgNotoship = []
for i in range(LibNo):
    bookscore = 0
    avgNotoship.append((len(BookIDCol[i])/ShipLim[i])- SignUp[i])
    for j in BookIDCol[i]:
        bookscore = bookscore + BookScore[j]
    totalBookscore_perlib.append(bookscore/ShipLim[i])

X = {v: k for v, k in enumerate(avgNotoship)}



sorted_libsignups = {k: v for k, v in sorted(X.items(), key=lambda x: x[1], reverse= True)}

sorted_lib = sorted(X.items(), key = lambda x: x[1], reverse= True)

print(sorted_lib)

def libscore(i):
    sorted_lib()

libans = [0]*len(sorted_lib)


def bookscore1(i):
    return -BookScore[i]

for i in BookIDCol:
    i.sort(key = bookscore1)

print(BookIDCol)

liborder = []
BookOrd = []
for i in sorted_lib: 
    liborder.append(i[0])

for i in range(len(liborder)):
    BookOrd.append(BookIDCol[liborder[i]])

print(liborder[0])

LibID = liborder

#  Print output data and create output file   
print("")
print("OUTPUT")


# computing the values using the heuru=istica equations
outputFile = open(file1 + "out" + ".txt", "w")
outputFile.write(str(len(LibID)))
outputFile.write("\n")
for l in range(len(LibID)):
    outputFile.write(str(LibID[l]))
    outputFile.write(" ")
    outputFile.write(str(len(BookOrd[l])))
    outputFile.write("\n")
    for m in range(len(BookOrd[l])):
        outputFile.write(str(BookOrd[l][m]))
        outputFile.write(" ")
    outputFile.write("\n")


outputFile.close()


inputFilesDirectory = "Input/"  # Location of input files
outputFilesDirectory = "Output/"  # Location of output files

fileNames = ["a_example", "b_read_on", "c_incunabula",
        "d_tough_choices", "e_so_many_books","f_libraries_of_the_world"]  # File names








