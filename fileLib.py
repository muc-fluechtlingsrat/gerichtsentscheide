class File:
    def __init__(self, filename, readMode = "r"):
        if filename[-4:] in [".csv",".tsv",".txt"]:
            self.filename = filename
            self.readMode = readMode
            self.file = open(filename, readMode)
            self.fileArray = []
            self.fileArrayExploded = []
            self.closed = False
    def explode(self, searchString):
        if self.fileArrayExploded != []: return self.fileArrayExploded
        for line in self.read():
            self.fileArrayExploded.append(explode(line,searchString))
        return self.fileArrayExploded
    def openFile(self):
        if self.closed: self.file = open(self.filename, self.readMode)
        else: print("File already open")
    def close(self):
        if not self.closed: self.file.close()
        else: print("File already closed")
    def read(self):
        if self.fileArray != []: return self.fileArray
        for line in self.file:
            self.fileArray.append(strip(line, "\n"))
        return self.fileArray

class CSV:
    def __init__(self,filename, readMode = "r"):
        if filename[-4:] == ".csv" or filename[-4:] == ".tsv":
            self.file = File(filename, readMode)
            self.fileArray = []
            self.fileArrayExploded = []
    def explode(self, searchString):
        if self.fileArrayExploded != []: return self.fileArrayExploded
        self.fileArrayExploded = self.file.explode(searchString)
        return self.fileArrayExploded
    def openCSV(self): self.file.openFile()
    def close(self): self.file.close()
    def read(self):
        if self.fileArray != []:
            return self.fileArray
        for i in self.file.read():
            self.fileArray.append(strip(line," "))
        return self.fileArray

def explode(sourceString, searchString):
    liste = []
    string1 = ""
    string2 = ""
    for i in sourceString:
        if len(string2) == len(searchString):
            string1 += string2[0]
            string2 = string2[1:]
        string2 += i
        if string2 == searchString:
            if string1 != "":
                liste.append(string1)
                string1 = ""
            string2 = ""
    if string1 != "" or string2 != "":
        liste.append(string1+string2)
    return liste

def replace(sourceString, stringToBeCutOut, replacementString):
    liste = explode(sourceString, stringToBeCutOut)
    string = ""
    for i in liste:
        string += replacementString + i
    if sourceString[-len(stringToBeCutOut):] == stringToBeCutOut:
        string += replacementString
    return string[len(replacementString):]

def strip(sourceString, stringToBeRemoved):
    return replace(sourceString, stringToBeRemoved, "")
