# Welcome To QWhale Documentation.

Our service provides an easy way to store your data free on the MongoDB database.

There is tow main options to use our service\
1) Using the REST API\
    To activate...\
    ```
    $> https://qwhale.ml/activate/{YOUR-TOKEN}
    ```
    To deactivate...\
    ```
    $> https://qwhale.ml/deactivate/{YOUR-TOKEN}
    ```

2) Using the official library\
    The library is simple, all you need is a TOKEN that you can get from our website [here](http://qwhale.ml)\
    and that it! you are ready to work with our service.\

    The library works with [_pymongo_](https://github.com/mongodb/mongo-python-driver) so you can use it like you use to.\

    **code example**\
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
