import requests


response = requests.post(
    "http://localhost:8080/joke/invoke",
    json={'input': {'topic': 'Joe Briden'}}
)
print(response.json().get('output')['content'])
