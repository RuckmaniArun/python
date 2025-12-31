import requests

name="Ruckmani"
response=requests.get(f"https://api.agify.io?name={name}")
print(response.json())
print(response.status_code)