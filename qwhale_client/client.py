import requests
from pymongo import MongoClient
from pymongo.database import Database


__all__ = ["APIClient"]

API_URL = "http://qwhale.ml/api"


class APIClient:
    def __init__(self, token: str):
        if not self.verify_token(token):
            raise ValueError(f"Token: {token} is invalid.")
        self._token = token
        self._db_name = self._token.split(":")[0]
        self._session: requests.sessions.Session = requests.session()
        self._database_info = None
        self._mongo_client: MongoClient = None
        self.activated = False

    def verify_token(self, token: str) -> bool:
        if len(token) != 65 or token.count(":") != 1:
            return False
        return True

    @property
    def database_info(self):
        if self._database_info is None:
            raise ValueError("Database isn't activated.")
        return self._database_info

    def activate_database(self):
        result = self._session.get(API_URL+f"/activate/{self._token}")
        assert result.status_code == 200, result.json()

        activation_info = result.json()
        self._database_info = activation_info
        self.activated = True

    def deactivate_database(self):
        result = self._session.get(API_URL+f"/deactivate/{self._token}")
        assert result.status_code == 200, result.json()

        deactivation_info = result.json()
        return deactivation_info

    def get_database(self) -> Database:
        if self._database_info is None:
            self.activate_database()
        client = MongoClient(self.database_info["mongo_url"])
        self._mongo_client = client
        db = client.get_database(self._db_name)
        return db

    def close(self):
        try:
            self._mongo_client.close()
        finally:
            self.activated = False
            return self.deactivate_database()

    def __enter__(self) -> Database:
        self.activate_database()
        db = self.get_database()
        return db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
