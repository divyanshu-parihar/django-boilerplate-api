import requests
import json
url = 'http://127.0.0.1:8000/api/update/'

data = {
'id':1,
'email':"adityarana@gmail.com"
}


json_data=json.dumps(data)
# r= requests.post(url= url, data= json_data)


# r= requests.delete(url= url, data= json_data)
r= requests.patch(url= url, data= json_data)
print(r.text) 