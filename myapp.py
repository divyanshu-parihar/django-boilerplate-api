import requests
import json
url = 'http://127.0.0.1:8000/api/update/'

data = {
'id':2,
'name':'hello',
'age':13,
'phone_number':99999999999,
}


json_data=json.dumps(data)
# r= requests.put(url= url, data= json_data)


# r= requests.delete(url= url, data= json_data)
r= requests.patch(url= url, data= json_data)
print(r.text) 