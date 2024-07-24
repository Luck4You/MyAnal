import requests
import json
data_with={'token':'27993.NNBgQ3UdDg618ydAg',
      'qrraw':'t=20240714T1608&s=301.85&fn=7380440700428408&i=17605&fp=477946500&n=1'}
response = requests.post(f"https://proverkacheka.com/api/v1/check/get", data=data_with)
json_obj = response.json()['data']['json']
for obj in json_obj:
    print(obj)

