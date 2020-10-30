import os
import re
import glob
import sys

print('You can always type in \"stop\" to terminate the program.')

try:
    dirName = os.path.dirname(__file__)
    gotDirName = True
except:
    print('Cant get the directory of this python file.')
    gotDirName = False
inputName=None
while True:
    if inputName=='stop':
        sys.exit()
    txtList = glob.glob1(dirName,"*.txt")
    txtCounter = len(txtList)
    if gotDirName and txtCounter!=0: 
        if txtCounter>1:
            inputName=input('Found more than 1 \'.txt\' file on the same directory with this python file.\nPlease enter the name of the file that you wish to load.\n')
            fileName = os.path.join(dirName, inputName + ".txt")
        elif txtCounter==1:
            print('Found only 1 \'.txt\' file on the same directory with this python file.')
            txtFile = txtList[0]
            inputName=txtFile
            fileName = os.path.join(dirName, inputName)
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
        words[word]=words.get(word,0)+1
        wordCount+=1
print(inputName+" has "+str(len(words))+" unique words. ("+str(wordCount)+" words in total).")

wordList=[]
for key,val in words.items():
    wordList.append((val,key))
wordList=sorted(wordList,reverse=True)

gotNum=False
while gotNum==False:
    numTop=input("How many most used words do you want to see?\n")
    if numTop.isdigit():
        numTop=int(numTop)
        gotNum=True
    else:
        if numTop=='stop':
            sys.exit()    
        print('Please enter a valid number')
if numTop > 0:
    topList=wordList[:numTop]
    print('Here is a list of '+inputName+'\'s top '+str(numTop)+' most used words by order:')
    printLineCounter=0
    for word in topList:
        printLineCounter+=1
        printWord=str(word[1][0]).upper()+str(word[1][1:])
        print(str(printLineCounter) + ". \"" + printWord + "\" used " + str(word[0]) + " times.")
else:
    # If the number is 0 or less, make the user feel a little guilty. He should be ashamed.
    print('Ohh... OK... Nevermind than... :(')