import requests
import json

URL = "http://127.0.0.1:8000/api/deser_stu/"

data = {
    'name': 'Rahuls',
    'roll': 6,
    'city': 'fbd' 
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

data = r.json()
print(data)