import requests
import pandas as pd

#test qqraw = 't=20240714T1608&s=301.85&fn=7380440700428408&i=17605&fp=477946500&n=1'
def send_request_to_dict(qqraw: str):
    data_with={'token':'27993.NNBgQ3UdDg618ydAg',
        'qrraw':qqraw}
    response = requests.post(f"https://proverkacheka.com/api/v1/check/get", data=data_with) 
    json_obj = response.json()['data']['json']

    dict_with_items = dict
    for i, obj in json_obj['items']:

        print(obj['name'])
        print(obj['sum'])
        print(obj['quantity'])
        print(obj['price'])
        name = obj['name']
        sum = obj['sum']
        quantity = obj['quantity']
        price = obj['price']
        dict_with_items[f'item{1}'] = f'{name}, в количестве/весом {quantity} по цене {price}. \n Итоговая стоимость = {sum}'
    return dict_with_items

