import requests
import json
url = 'http://127.0.0.1:8000/api/update/'

data = {
'id':'5',
'name':'happy singh',
'age':13,
'phone_number':888888888888,
'father_name':'xyz'
}


json_data=json.dumps(data)
# r= requests.put(url= url, data= json_data)


# r= requests.delete(url= url, data= json_data)
r= requests.put(url= url, data= json_data)
print(r.text) 