import json
import termcolor

# -- Open the json file
f = open("ex1.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
ex1 = json.load(f)

person = ex1['Person']
termcolor.cprint("Number of people : ", 'green', end='')
print(len(person))

for i, info in enumerate(person):
    termcolor.cprint("  Person {}:".format(i+1), 'blue')

    termcolor.cprint("    Name: ", 'red', end='')
    print(info['firstname'])
    termcolor.cprint("    Lastname: ", 'red', end='')
    print(info['lastname'])
    termcolor.cprint("    Age: ", 'red', end='')
    print(info['age'])
    termcolor.cprint("    Phones available: ", 'red', end='')
    print(len(info["phone"]))

for i, num in enumerate(person):
    termcolor.cprint(   "Phone", 'red', end='')
    print(i)
    termcolor.cprint(   "Type", 'red', end='')
    print(num["type"])
    termcolor.cprint(   "Number", 'red', end='')
    print(num["number"])





