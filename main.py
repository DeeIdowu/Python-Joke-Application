from urllib import request

r = request.urlopen("http://www.google.com")
"""Printing the http request, getcode to receive 200 status and read to read content:"""
print(r.getcode())
print(r.read())
