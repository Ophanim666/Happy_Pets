from urllib.request import urlopen
import json 

url = "https://random-data-api.com/api/users/random_user"

response = urlopen(url)
data = json.loads(response.read())
for i in data:
    print(i)
    break