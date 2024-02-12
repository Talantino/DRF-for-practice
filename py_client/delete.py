import requests

product_id = input("What is the product id you want to use?")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not valid')

if product_id:
    endpoint = "http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)