import requests

url = "https://example.com"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Headers:")
print(response.headers)
