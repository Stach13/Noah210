# Our challenge: read in multiple text files from a directory:
# Our resource: The Python os module + a handy code example:
#  https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
import spacy
# nlp = spacy.cli.download("en_core_web_md")
nlp = spacy.load('en_core_web_md')

import os

##############################
# OBJECTIVE: Find out which words in my document are most similar to a particular word of interest
# How to find this using spaCy similarity vectors?

# Helpful resource for spaCy similarity calculation based on a selected word:
# https://stackoverflow.com/questions/55921104/spacy-similarity-warning-evaluating-doc-similarity-based-on-empty-vectors
##############################

# ebb: The os module comes with python so you probably don't have to install it.
# Just add the import line

# commenting out in Pycharm: find keystroke under Code >> Comment with linecomment

# ebb: Identify a file directory with text files to explore:
# ebb: os.cwd returns the current working directory path

workingDir = os.getcwd()
print("current working directory: " + workingDir)

# os.listdir lists files and folders inside a path:
insideDir = os.listdir(workingDir)
print("inside this directory are the following files AND directories: " + str(insideDir))

# use os.path.join to connect the subdirectory to the working directory:
CollPath = os.path.join(workingDir, 'textCollection')
print(CollPath)

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)
# ebb: add that utf8 encoding argument to the open() function to ensure that reading works on everyone's systems
# this all succeeds if you see the text of your files printed in the console.
        tokens = nlp(stringFile)
        # playing with vectors here
        vectors = tokens.vector
        # 2023-02-26 ebb: The line below is where you set your word of interest.
        wordOfInterest = nlp(u'panic')
        # print(wordOfInterest, ': ', wordOfInterest.vector_norm)

        # Now, let's open an empty dictionary! We'll fill it up with the for loop just after it.
        # The for-loop goes over each token and gets its values
        highSimilarityDict = {}
<<<<<<< HEAD
        sortedhighSimilarityDict = sorted(highSimilarityDict)

        print(sortedhighSimilarityDict)
=======
        # sortedhighSimilarityDict = sorted(highSimilarityDict)
        # 2023-02-06 ebb: The highSimlarityDict needs to be empty up here.
        # ebb: It will be populated by the for loop. This is a pretty common Python strategy
        # to create an empty data structure and then run a for-loop to fill it.
>>>>>>> 7ce464b191861fdd457b0d4f37f053b812498437

        for token in tokens:
            if(token and token.vector_norm):
                # if token not in highSimilarityDict.keys(): # Alas, this did not work to remove duplicates from my dictionary. :-(
                if wordOfInterest.similarity(token) > .5:
                    highSimilarityDict[token] = wordOfInterest.similarity(token)
                    # The line above creates the structure for each entry in my dictionary.
                         # print(token.text, "about this much similar to", wordOfInterest, ": ", wordOfInterest.similarity(token))
        print("This is a dictionary of words most similar to the word " + wordOfInterest.text + " in this file.")
        print(highSimilarityDict)


        highSimilarityReduced = {}
        for key, value in highSimilarityDict.items():
            if value not in highSimilarityReduced.values():
                highSimilarityReduced[key] = value
        print(highSimilarityReduced)
        print(len(highSimilarityReduced.items()), " vs ", len(highSimilarityDict.items()))

        # ebb: For this next part, it's YOUR TURN to write some modifying code.
        # We should sort the highSimilarityReduced dictionary by values from high to low,
        # but sorting is a little tricky because we need to isolate the **value**
        # not the key.
        # HOW TO DO IT? SEE https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
        # NOTE: After you sort, your results won't be a dictionary any more!
        # So you should read the WHOLE tutorial to see how to convert this back into a dictionary again
        # and do that in your code here.

# ebb: This controls our file handling as a for loop over the directory:
for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)
