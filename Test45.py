# Improting the required module
import requests

r = requests.get("https://codewithcurious.com")
print (r.text)