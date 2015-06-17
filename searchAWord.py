from sys import argv

script, filename = argv

# Fetching the any word to search in a text file
print "Type the search word: "
searchWord = raw_input(">")

# Opening the file given by the user
with open(filename) as inf:
    # Iterating each line then fetch the line number
    for lineNumber, line in enumerate(inf, 1):
        line = line.lower()
        if searchWord in line:
            print 'Yes we found a word %r, in line %d, and in the %r file.' %(searchWord, lineNumber, filename)
        # If no match in each lines for the searched word
        else:
            print 'No %r in this line %r.' %(searchWord, lineNumber)
