def chessNotation(notation):
    
    # -- split passed notation into list, then turn numbers into all 1s -- #
    notations = notation.split('/')
    notations = divideEmptySpaces(notations)
    
    # -- initialize rotatedNotation list and compiledNotation string -- #
    rotatedNotation = [""] * 8
    compiledNotation = ""  
    
    # -- Create new rotatedNotation from notations list -- #
    for row in notations:       
        i = 0
        while i < 8:
            rotatedNotation[i] += row[i]
            i += 1

    # -- Reverse rotatedNotation, and all notations to compiledNotation string -- #
    q = 0
    while q < 8:
        rotatedNotation[q] = addEmptySpaces(rotatedNotation[q])[::-1] # Reverse Notation [::-1] using extended slice syntax
        compiledNotation += rotatedNotation[q] + '/'
        q += 1
    
    # -- return compiledNotation string -- #    
    return compiledNotation[:-1]
        

def divideEmptySpaces(notations):
    parsedNotations = []
    
    for row in notations:
        
        addedRow = ""

        for square in row:

            if square.isalpha():
                addedRow += square

            if not square.isalpha():
                i = 0
                while i < int(square):
                    addedRow += "1"
                    i += 1
        parsedNotations.append(addedRow)
        
    return parsedNotations        
            
        
def addEmptySpaces (row):
    addedRow = ""
    emptySpaceCount = 0  
    
    for square in row:
        if square.isalpha():
            if emptySpaceCount != 0:
                addedRow += str(emptySpaceCount)
                emptySpaceCount = 0                
            addedRow += square
            
        if not square.isalpha():
            emptySpaceCount += 1
            
    if not row[-1].isalpha():
        addedRow += str(emptySpaceCount)
    
    return addedRow
