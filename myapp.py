import requests
import json
url = 'http://127.0.0.1:8000/api/'

data = {
'id':'5',
'name':'happy singh',
'age':13,
'phone_number':888888888888,
'father_name':'xyz'
}
# we have to made a header to specify the content-type
header = {'contenc-Type':"application/json"}

json_data=json.dumps(data)
# r= requests.put(url= url, data= json_data)


# r= requests.delete(url= url, data= json_data)
r= requests.post(headers= header,url= url,data = data)
print(r.text) 