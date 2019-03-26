# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json
from Seq import Seq
import collections
PORT = 80
SERVER = 'rest.ensembl.org'


print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

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
sequence = json.loads(data1)
gene = Seq(sequence['seq'])

print("Welcome!! We are working with the sequence: {}".format(gene.strbases))
print("The FRAT1 gene is {}".format(len(gene.strbases)), "bases long") #printing how long the sequence is
count_T = gene.count("T") #counting the number of bases
print("There is a total of {}".format(count_T), "thymine bases.")
popular = collections.Counter(gene.strbases).most_common(1)[0] #finding the most common base

print("The most frequent character in the sequence is: ", popular[0], "and the percentage is: {}".format(gene.perc(popular[0])))
perc_a = gene.perc("A") #making all the percentages of every base
perc_t = gene.perc("T")
perc_g = gene.perc("G")
perc_c = gene.perc("C")
print("The percentage of base A is: {}".format(perc_a))
print("The percentage of base T is: {}".format(perc_t))
print("The percentage of base G is: {}".format(perc_g))
print("The percentage of base C is: {}".format(perc_c))






