import json
import termcolor

# -- Open the json file
f = open("ex1.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
ex1 = json.load(f)

person = ex1['Person']
termcolor.cprint("Number of people : ", 'green', end='')
print("The total number of people is: {}".format(len(person)))

for a, element in enumerate(person):
    termcolor.cprint("    Name: ", 'red', end='')
    print(element['firstname'])
    termcolor.cprint("    Lastname: ", 'red', end='')
    print(element['lastname'])
    termcolor.cprint("    Age: ", 'red', end='')
    print(element['age'])
    termcolor.cprint("    Phones available: ", 'red', end='')
    print(len(element["phone"]))


    for i, num in enumerate(element['phone']):
        termcolor.cprint(   "Phone {} ".format(i), 'red', end='')
        termcolor.cprint(   "Type: ", 'red', end='')
        print(num["type"])
        termcolor.cprint(   "Number: ", 'red', end='')
        print(num["number"])

