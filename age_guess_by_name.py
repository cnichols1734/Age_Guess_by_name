import requests

# Get the person's name
name = input("Enter your first name and I will attempt to guess your age: ")

# Make the API request
url = "https://api.agify.io"
params = {"name": name, "country_id": "US"}
headers = {
    "X-API-Key": "your-api-key"
}
response = requests.get(url, params=params, headers=headers)

# Parse the JSON response
data = response.json()

# Print the data
print(data)



