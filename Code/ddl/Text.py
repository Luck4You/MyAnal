import requests
import json
data_with={'token':'27993.NNBgQ3UdDg618ydAg',
      'qrraw':'t=20240701T2356&s=645.13&fn=7282440700345004&i=143909&fp=3484327089&n=1'}
response = requests.post(f"https://proverkacheka.com/api/v1/check/get", data=data_with)
print(type(response.json()))
json_obj = response.json()
for obj in json_obj:
    print(obj)
