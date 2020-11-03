from urllib import request

"""Making API call and working with json objects for random jokes"""
url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
"""Printing the http request, getcode to receive 200 status and read to read content:"""
print(r.getcode())
print(r.read())
