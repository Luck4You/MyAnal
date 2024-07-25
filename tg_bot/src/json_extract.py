import requests
import pandas as pd

#test qqraw = 't=20240701T2356&s=645.13&fn=7282440700345004&i=143909&fp=3484327089&n=1'
def send_request_to_dict(qqraw: str):
    data_with={'token':'27993.7QrCC3B4OgsTOKA2m',
        'qrraw':qqraw}
    response = requests.post(f"https://proverkacheka.com/api/v1/check/get", data=data_with) 
    json_obj = response.json()['data']['json']

    dict_with_items = []
    for obj in json_obj['items']:
        print(obj['name'])
        print(obj['sum'])
        print(obj['quantity'])
        print(obj['price'])
        name = obj['name']
        sum = obj['sum']
        quantity = obj['quantity']
        price = obj['price']

        string_to_return = f'{name}, в количестве/весом {quantity} по цене {price}. \n Итоговая стоимость = {sum}'
        dict_with_items.append(string_to_return)

    return dict_with_items

