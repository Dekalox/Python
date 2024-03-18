# import requests

# link = "http://simonrosenthal.de/"
# f = requests.get(link)
# print (f.text)

from urllib.request import urlopen

link = "http://simonrosenthal.de"

f = urlopen(link)
myfile = f.read()
print (myfile)