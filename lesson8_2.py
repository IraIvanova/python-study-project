import pymongo
import requests

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["mydb"]
quotes_collection = database["quotes"]

url_data = "https://dummyjson.com/quotes?limit=100"

response = requests.get(url=url_data)
data_from_web = response.json()
quotes = data_from_web["quotes"]

quotes_collection.insert_many(quotes)

query = {"author": "Albert Einstein"}
albert_einstein_quotes = quotes_collection.find(query)

query2 = {'quote': {'$regex': 'success'}}
quotes_with_word_success = quotes_collection.find(query2)

filter_criteria = {"author": "Mark Twain"}
query3 = {"$set": {"favorite": True}}
update_result = quotes_collection.update_many(filter_criteria, query3)

query4 = {"author": "Vincent Van Gogh"}
quotes_collection.delete_many(query4)

quotes_collection.drop()
