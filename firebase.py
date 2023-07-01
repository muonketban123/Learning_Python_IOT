
import requests as re

url  = "https://myproject-8695e-default-rtdb.asia-southeast1.firebasedatabase.app/test.json"

json = {"int" : 2}

s = re.put(url = url, json = json)

