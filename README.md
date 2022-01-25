# qwhale-client

## This is the official python client library

The library is simple, all you need is a TOKEN that you can get from our website hare
and that it! you are ready to work with our service.


The library works with [_pymongo_](https://github.com/mongodb/mongo-python-driver) so you can use it like you use to.

**code example**
```python
from qwhale_client import APIClient

TOKEN = "<YOUR API TOKEN>"

client = APIClient(TOKEN)

with client as database:
    print(client.activated)  # -> True
    database["test"].insert_one({"key": "value", "extra": "123456"})
    document = database["test"].find_one({"key": "value"})
    print(document)  # -> {"_id": ObjectId(...), "key": "value", "extra": "123456"}

print(client.activated)  # -> False
```

**Another code example**
```python
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
```
