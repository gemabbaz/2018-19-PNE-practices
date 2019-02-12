#Adding some info

FILENAME = "mynotes.txt"

f= open(FILENAME, 'r')

contents = f.read()

print("File: {}".format(f.name))
print("{}".format(contents))

f.close()

f = open(FILENAME, "a")
f.write("Helloooooo!!! ")

f.close()

print("End")