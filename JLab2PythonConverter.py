#cells
#CELL[1]
import re
import math

#CELL[2]
docs = []

#CELL[3]
CELLCOUNTER = 1

def setCELLCOUNTER(n: int):
    global CELLCOUNTER 
    CELLCOUNTER = n

def getCELLCOUNTER() -> int:
    global CELLCOUNTER
    return(CELLCOUNTER)

#CELL[4]
SOURCE = False

def setSOURCE(b: bool):
    global SOURCE 
    SOURCE = b

def getSOURCE() -> bool:
    global SOURCE
    return(SOURCE)

#CELL[5]
PATTERN = re.compile("\\\\+")

def getPATTERN():
    global PATTERN
    return(PATTERN)

#CELL[6]
def line2py(line):
    if getSOURCE():
        if line == "   ]\n":
            setSOURCE(False)
            return("\n")
        line = line[line.index("\"") +1 : line.rindex("\"")]
        if line[-2:] == "\\n":
            line = line[:-2]
        p = getPATTERN()
        groups = [(group[0], group[1] -1, group[1] - group[0]) for group in [match.span() for match in p.finditer(line)]]
        temp = 0
        result = ""
        for group in groups:
            result += line[temp:group[0]] + "".join(["\\" for i in range(math.floor(group[2]) //2 )])
            temp = group[1] + 1
        if groups:
            result+= line[groups[-1][1]+1:]
            line = result
        return(line + "\n")
    if line == " \"cells\": [\n":
        return("#cells\n")
    if line == "   \"source\": [\n":
        setSOURCE(True)        
        cellcounter = getCELLCOUNTER()
        setCELLCOUNTER(cellcounter + 1)
        return(f"#CELL[{cellcounter}]\n")
    return("")

#CELL[7]
def ipynb2py(docs):
    for doc in docs:
        f = open(doc, "r")
        lines = f.readlines()
        #print(lines)
        f = open(doc[:-5] + "py", "w")
        setCELLCOUNTER(1)
        for line in lines:
            f.write(line2py(line))
                

#CELL[8]
if __name__== "__main__":
    ipynb2py(docs)

