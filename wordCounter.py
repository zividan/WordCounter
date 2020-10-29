import os
import re
try:
    dirName = os.path.dirname(__file__)
    gotDirName = True
except:
    print('Cant get the directory of this python file.')
    gotDirName = False

while True:
    if gotDirName:
        inputName=input('Please enter a \'.txt\' file name that is on the same directory with this python file.\n')
        fileName = os.path.join(dirName, inputName + ".txt")
    else:
        inputName=input('Please enter a complete \'.txt\' file path.\n')
        fileName=inputName

    print('Loading: '+fileName) 
    try:
        fileHandle = open(fileName)
        break
    except:
        print('File could not be loaded.')
        continue

wordCount=0
words={}
for line in fileHandle:
    # Get rid of punctuation, weird charecters and uppercase before splitting
    line=re.sub(r"[^A-Za-z0-9']"," ",line,flags = re.I)
    line=line.lower()
    line=line.split()
    for word in line:
        # Adds new word to the dictionary with value of 1, or if it already exists just adds 1 to it's value
        words[word]=words.get(word,0)+1
        wordCount=wordCount+1
print(inputName+" has "+str(len(words))+" unique words. ("+str(wordCount)+" words in total).")

wordList=[]
for i in range(len(words)):
    bigWord=None
    bigVal=0
    for key,val in words.items():
        if val>bigVal:
            bigWord=key
            bigVal=val
    wordList.append([bigWord,bigVal])
    del words[bigWord]

gotNum=False
while gotNum==False:
    numTop=input("How many most used words do you want to see?\n")
    if numTop.isdigit():
        numTop=int(numTop)
        gotNum=True
    else:
        print('Please enter a valid number')
if numTop > 0:
    topList=wordList[:numTop]
    print('Here is a list of '+inputName+'\'s top '+str(numTop)+' most used words by order:')
    printLineCounter=0
    for word in topList:
        printLineCounter=+1
        printWord=str(word[0][0]).upper()+str(word[0][1:])
        print(str(printLineCounter) + ". \"" + printWord + "\" used " + str(word[1]) + " times.")
else:
    # If the number is 0 or less, make the user feel a little guilty. He should be ashamed.
    print('Ohh... OK... Nevermind than... :(')
