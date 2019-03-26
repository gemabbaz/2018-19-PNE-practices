# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8004
SERVER = 'localhost'


print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

# Print all the numbers
for element in person:
    termcolor.cprint("Name: ", 'red', end="")
    print(person['firstname'], person['lastname'])
    termcolor.cprint("Age: ", 'red', end="")
    print(person['age'])
    termcolor.cprint("    Phones available: ", 'red', end='')
    print(len(element["phone"]))

    for i, num in enumerate(phone):
        termcolor.cprint(   "Phone {} ".format(i), 'red', end='')
        termcolor.cprint(   "Type: ", 'red', end='')
        print(num["type"])
        termcolor.cprint(   "Number: ", 'red', end='')
        print(num["number"])
