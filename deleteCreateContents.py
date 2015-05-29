# This will delete the contents of the file then the program will allow you to create new contents
# of the file.

from sys import argv

script, filename = argv

print "We will erase first the contents of %s file" %filename
print "Press CTRL-C to cancel."
print "Hit ENTER to proceed."
raw_input("? ")

print "Opening the file: "
print "*" * 10;
target = open(filename, "w")

print "Truncating the file contents: Goodbye!"
target.truncate()

print "Enter here the new contents of %r file" %filename
newContent = raw_input();
print "Now saving new contents: "
print "*" * 10
target.write(newContent)
print "Done saving new contents."
target.close()

