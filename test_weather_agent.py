import requests

response = requests.post("http://127.0.0.1:9999/agent", json={"input": "What’s the weather in London?"})
print("Status Code:", response.status_code)
print("Response:", response.json())
