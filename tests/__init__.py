import requests

url = "https://api.cloud.deepset.ai/api/v2/custom_components"

files = { "file": ("custom_component.zip", open("custom_component.zip", "rb"), "application/x-zip-compressed") }
headers = {
    "accept": "application/json",
    "authorization": "Bearer <DEEPSET_CLOUD_API_KEY>"
}

response = requests.post(url, files=files, headers=headers)

print(response.text)