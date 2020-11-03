from urllib import request
import json

"""Making API call and working with json objects for random jokes. 
Removal of s in http deters use of SSL certification"""
url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
"""Printing the http request, getcode to receive 200 status and read to read content:"""
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)


"""Looping through jsonData to display setup and punchline"""


class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline


jokes = []

for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)
