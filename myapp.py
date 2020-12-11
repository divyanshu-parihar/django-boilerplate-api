import requests
import json
url = 'http://127.0.0.1:8000/api/'

data = {
'id':6,
'name':'aditya singh',
'age':14,
'phone_number':788888888888,
'father_name':'xyz'
}
# we have to made a header to specify the content-type
header = {
    'content-Type':"application/json"
}

json_data=json.dumps(data)
# r= requests.put(url= url, data= json_data)


# r= requests.delete(url= url, data= json_data)
r= requests.post(headers= header,url= url,data = data)
data = r.json()
print(data) 