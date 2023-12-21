import requests
import json

url_data = "https://dummyjson.com/quotes?limit=100"

response = requests.get(url=url_data)
data_from_web = response.json()
quotes = data_from_web["quotes"]
filtered_quotes = []

for quote in quotes:
    if quote["id"] == 4:
        filtered_quotes.append(quote)

with open("data/quotes_data.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(filtered_quotes))
