import requests

url = "http://127.0.0.1:8000/apitest/testAll/"

payload = "{\"selected_product_id\": 3}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
