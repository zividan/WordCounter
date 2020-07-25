# Try to get the relative path to this file
# (I'm using try/except because it might cause problems on some opareting systems? I'm not sure but it's better to be safe than tracebacked)
try:
    # Get the path to this python file's directory
    import os
    dirname = os.path.dirname(__file__)
    # initialize variable to indicate that we got the relative path
    gotdirname = True
except:
    print('Cant get the directory of this python file.')
    # initialize variable to indicate that we didn't got the relative path
    gotdirname = False
# A loop to get a valid file name from the user
while True:
    # If we have the relative path, just ask for a file name
    if gotdirname:
        # Get a file name from the user
        inputname=input('Please enter a \'.txt\' file name that is on the same directory with this python file.\n')
        # Add the file name we got from the user to the path, and add the '.txt' file format to the end of it
        filename = dirname+"/"+inputname+'.txt'
     # If we don't have the relative path, the user has to type the entire path like a peasant :(
    else:
        # Get a whole file path from the user
        inputname=input('Please enter a complete \'.txt\' file path.\n')
        # Set the same value to filename because we use both of them (It's just cosmetic, but they are different when we have the relative path!)
        filename=inputname
    # Try to open the file
    print('Loading: '+filename) 
    try:
        filehandle = open(filename)
        # If there is no traceback we can stop the loop and keep going
        break
    except:
        # On a traceback go back to start and ask for a new file name
        print('File does not exist.')
        continue
# Import the regex module
import re
# Initialize a counter for words in total
wordcount=0
# Initialize a dictionary to count each unique word
words={}
# A loop to go over every line of the txt file
for line in filehandle:
    # Get rid of punctuation and weird charecters
    line=re.sub(r"[^A-Za-z0-9']"," ",line,flags = re.I)
    # Ignore UpperCase, convert all to LowerCase
    line=line.lower()
    # Split the line to a list of words
    line=line.split()
    # A loop to go over every word in the list
    for word in line:
        # Add unique word to the dictionary with value of 1, if it exist just add 1 to it
        words[word]=words.get(word,0)+1
        # Add 1 to the total word count
        wordcount=wordcount+1
# Print the total and unique word counts to the user
print(inputname+" has "+str(len(words))+" unique words. ("+str(wordcount)+" words in total).")
# initialize a list of words
wordlist=[]
# A loop to go over the unique words in the dictionary (using the range method because we're going to change the dictionary size)
for i in range(len(words)):
    # Initialize variables to save most used word so far, and times it was used
    bigword=None
    bigval=0
    # A loop to go over the items left in the dictionary
    for key,val in words.items():
        # Assign values of the most used word to the variables
        if val>bigval:
            bigword=key
            bigval=val
    # When finished going over all of the words, add the most used word to the list
    wordlist.append([bigword,bigval])
    # Now delete this word from the dictionary before the loop starts again
    del words[bigword]
    # The loop starts again to add the next most used word to the list, by order
# A loop to ask the user how many results to show until he gives a valid number
while True:
    # Ask the user for a number
    numtop=input("How many most used words do you want to see?\n")
    try:
        # convert the number to an integer
        numtop=int(numtop)
        # If There's no traceback it's a valid number - break the loop
        break
    except:
        # If there's a traceback ask for a valid number and start the loop again
        print('Please enter a number')
# Check if number is bigger than 0
if numtop > 0:
    # Initialize a new list, Assigning the previous list sliced up to the number of results to show to the user
    toplist=wordlist[:numtop]
    # Print a headline for the list
    print('Here is a list of '+inputname+'\'s top '+str(numtop)+' most used words by order:')
    # Initialize a counter to print result number
    printlinecounter=0
    # A loop to go over the sliced list
    for word in toplist:
        # Add 1 to the counter
        printlinecounter=printlinecounter+1
        # Format the word to print pretty (first letter UpperCased)
        printword=str(word[0][0]).upper()+str(word[0][1:])
        # Print the result line
        print(str(printlinecounter) + ". \"" + printword + "\" used " + str(word[1]) + " times.")
# If the number is 0 or less, make the user feel a little guilty. He should be ashamed.
else:
    print('Ohh... OK... nevermind than... :(')