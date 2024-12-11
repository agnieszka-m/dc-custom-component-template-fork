import requests

url = "https://api.cloud.deepset.ai/api/v2/custom_components"

files = { "file": ("custom_component.zip", open("custom_component.zip", "rb"), "application/zip") }
headers = {
    "accept": "application/json",
    "authorization": "Bearer api_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3NTQ1YzBhYi0xNTA2LTQ3MGUtYmY4YS04YTIxMTNiY2UzMGZ8NjQzY2Y5YTlmNzExNDg0MmUwNzk5ZDQ3IiwiZXhwIjoxNzM4Mjc4MDAwLCJhdWQiOlsiaHR0cHM6Ly9hcGkuY2xvdWQuZGVlcHNldC5haSJdfQ.jcQMPeb3Qo18425jdr_NeEv6ZGXEqHJbpG7hNU3Sohs"
}

response = requests.post(url, files=files, headers=headers)

print(response.text)