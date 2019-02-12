#Reading a file located in our local filesystem

NAME = "mynotes.txt"

myfile = open(NAME, 'r')

print("Print: file opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))
print("The end!")

myfile.close()