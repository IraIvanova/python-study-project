import requests

url_carts = 'https://dummyjson.com/carts'

response = requests.get(url=url_carts)
data_from_web = response.json()
carts = data_from_web['carts']

for cart in carts:
    if cart['userId'] == 56:
        products = cart['products']
        for product in products:
            if product['discountPercentage'] > 15:
                print(product['title'])
