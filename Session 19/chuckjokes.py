import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = {"/jokes/count", "/categories", "/jokes/random"}

METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
jokes_count = 0
cat_count = 0
cats = []
random = ""

for i in ENDPOINT:
    conn.request(METHOD, i, None, headers)
    # -- Print the status
    r1 = conn.getresponse()
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)
    text_json = r1.read().decode("utf-8")
    chuck = json.loads(text_json)
    if 'count' in i:
        jokes_count = chuck['value']
    elif 'categories' in i:
        cats = chuck['value']
        cat_count = len(cats)
    elif 'random' in i:

        random = (chuck['value'])['joke']
    else:
        print("ERROR")


    # -- Read the response's body and close
    # -- the connection
    conn.close()

    # -- Optionally you can print the
    # -- received json file for testing
    # print(text_json)

    # -- Generate the object from the json file
    cat = json.loads(text_json)

    # -- Print the received URL
print("Number of jokes", jokes_count)
print("List of categories", cats)
print("Number of categories", cat_count)
print("Random joke: ", random)