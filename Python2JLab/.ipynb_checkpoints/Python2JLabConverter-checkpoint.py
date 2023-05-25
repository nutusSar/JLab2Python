#cells
#CELL[1]
docs = [""]

#CELL[2]
CELLCOUNTER = 1

def getCELLCOUNTER() -> int:
    global CELLCOUNTER
    return(CELLCOUNTER)

def setCELLCOUNTER(n: int):
    global CELLCOUNTER
    CELLCOUNTER = n

#CELL[3]
SOURCE = False

def getSOURCE() -> bool:
    global SOURCE
    return(SOURCE)

def setSOURCE(b: bool):
    global SOURCE
    SOURCE = b

#CELL[4]
INSOURCE = False

def getINSOURCE() -> bool:
    global INSOURCE
    return(INSOURCE)

def setINSOURCE(b: bool):
    global INSOURCE
    INSOURCE = b

#CELL[5]
METADATA = False

def getMETADATA() -> bool:
    global METADATA
    return(METADATA)

def setMETADATA(b: bool):
    global METADATA
    METADATA = b

#CELL[6]
def line2ipynb(line):
    if line == "#cells\n":
        line = "{\n \"cells\": [" + "\n"
        return(line)
    if line == f"#CELL[{getCELLCOUNTER()}]\n":
        setSOURCE(True)
        setINSOURCE(False)
        line =  "  {\n   \"cell_type\": \"code\",\n   \"execution_count\": " + str(getCELLCOUNTER()) + ",\n   \"id\": \""+ str(getCELLCOUNTER()) + "\",\n   \"metadata\": {},\n   \"outputs\": [],\n   \"source\": [\n"
        if getCELLCOUNTER() > 1:
            line = "\n   ]\n  },\n"  + line
        setCELLCOUNTER(getCELLCOUNTER() + 1)
        return(line)
    if getMETADATA():
        return(line[2:])
    if line == "####[BELOW SECTION IS FOR Jupyter-Lab]\n":
        line = "\n   ]\n  }\n ],\n"
        setSOURCE(False)
        setINSOURCE(False)
        setMETADATA(True)
        return(line)
    if getSOURCE():
        line = line.replace("\\", "\\\\")[:-1]
        line = "   \"" + line.replace("\"", "\\\"") + "\\n\""
        if getINSOURCE():
            line = ",\n" + line
            return(line)
        setINSOURCE(True)
        return(line)
    return("")

#CELL[7]
def py2ipynb(docs):
    for doc in docs:
        f = open(doc, "r")
        lines = f.readlines()
        f = open(doc[:-2] + "ipynb", "w")
        setCELLCOUNTER(1)
        setINSOURCE(False)
        setSOURCE(False)
        setMETADATA(False)
        for line in lines:
            f.write(line2ipynb(line))
        

#CELL[8]
if __name__ == "__main__":
    py2ipynb(docs)

####[BELOW SECTION IS FOR Jupyter-Lab]##  "kernelspec": {
##   "display_name": "Python 3 (ipykernel)",
##   "language": "python",
##   "name": "python3"
##  },
##  "language_info": {
##   "codemirror_mode": {
##    "name": "ipython",
##    "version": 3
##   },
##   "file_extension": ".py",
##   "mimetype": "text/x-python",
##   "name": "python",
##   "nbconvert_exporter": "python",
##   "pygments_lexer": "ipython3",
##   "version": "3.11.2"
##  }
## },
## "nbformat": 4,
## "nbformat_minor": 5
##}
