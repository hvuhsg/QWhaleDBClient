from qwhale_client import APIClient

TOKEN = "<YOUR API TOKEN>"

client = APIClient(TOKEN)

database = client.get_database()
print(client.activated)  # -> True

database["test"].insert_one({"key": "value", "extra": "123456"})
document = database["test"].find_one({"key": "value"})
print(document)  # -> {"_id": ObjectId(...), "key": "value", "extra": "123456"}

print(client.close())  # -> {'data_saved': True}
print(client.activated)  # -> False
