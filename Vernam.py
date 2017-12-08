def enterPlaintext():
    print("Alphabet wraparound has been disabled due to instability.")
    print("All text will be converted to lowercase")
    plaintext = input("Enter plaintext: ")
    plaintext = plaintext.replace(' ','')
    return plaintext
    



def makeNumberArray(plaintext):
    key = []
    print('Enter a one time pad of', len(plaintext), 'numbers (Between 1 and 128)')
    for i in range(0,len(plaintext)):
        key.append(input('- '))
    return key

def charToBinary(plaintext):
    letList = []
    #converts character to ascii value and then binary equivilent
    for char in plaintext:
        num = ord(char)
        binaryNum = bin(num)
        binaryNum = list(binaryNum)
        del binaryNum[0:2]
        binaryNum = "".join(binaryNum)
        letList.append(binaryNum)
    return letList

def numToBinary(key):
    keyList = []
    #converts numbers to 7-bit binary
    for g in key:
        step = int(g)
        binStep = bin(step)
        binStep = list(binStep)
        del binStep[0:2]
        binStep = "".join(binStep)
        if len(binStep)<7:
            add = 7 - len(binStep)
            binStep = ('0'*add)+binStep
        keyList.append(binStep)
    return keyList

def logicalXOR(letList,keyList):
    zList = []
    encryptedList = []
    for item,item2 in zip(letList,keyList):
        for x,y in zip(item,item2):
            #this performs a logical XOR
            z = (int(x) and not int(y)) or (not int(x) and int(y))
            zList.append(z)
    for i in zList:
        if i == True:
            encryptedList.append('1')
        else:
            encryptedList.append('0')
    return encryptedList
            
def separateArray(encryptedList):
    letters = []
    while encryptedList:
        letters.append(encryptedList[0:7])
        del encryptedList[0:7]
    return letters

def binaryToDenary(letters):
    ordValue = []
    for l in letters:
        l = ("".join(l))
        binaryValue = l
        n= len(binaryValue)
        denary = 0
        for i in range(1,n+1):
            denary = denary+ int(binaryValue[i-1])*2**(n-i)
        ordValue.append(denary)
    return ordValue

def displayEncryptedWord(ordValue):
    finalList = []
    for m in ordValue:
        m = chr(m)
        finalList.append(m)
    encryptedWord = "".join(finalList)
        
    print ('Encrypted text:',encryptedWord)        
        
    

def menu():
    global runProgram
    plaintext = enterPlaintext()
    key = makeNumberArray(plaintext)
    letList = charToBinary(plaintext)
    keyList = numToBinary(key)
    encryptedList = logicalXOR(letList,keyList)
    letters = separateArray(encryptedList)
    ordValue = binaryToDenary(letters)
    displayEncryptedWord(ordValue)
    choice = input("Would you like to quit(Y/N)?: ").upper()
    if choice == "N":
        runProgram = True
    else:
        runProgram = False


runProgram = True
while runProgram:
    menu()
