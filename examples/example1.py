from client import APIClient

TOKEN = "904c4c34756b26cea3a34e7229004bf0:487f82b28d94f9f215fabb74846ce660"

client = APIClient(TOKEN)

with client as database:
    print(client.activated)  # -> True
    database["test"].insert_one({"key": "value", "extra": "123456"})
    document = database["test"].find_one({"key": "value"})
    print(document)  # -> {"_id": ObjectId(...), "key": "value", "extra": "123456"}

print(client.activated)  # -> False
