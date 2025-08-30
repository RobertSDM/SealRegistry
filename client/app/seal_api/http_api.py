import requests

from app.constants import API_ENDPOINT
from app.exceptions import APIError
from .interface import SealAPI
from requests.exceptions import ConnectionError


class HTTPSealAPI(SealAPI):
    @staticmethod
    def check(seal: int):
        try:
            resp = requests.get(API_ENDPOINT + f"/transport/seal/check?seal={seal}")

            return resp.ok
        except ConnectionError as e:
            raise APIError("Could not establish a connection to the server")

    @staticmethod
    def register(seal: int) -> bool:
        try:
            resp = requests.post(API_ENDPOINT + f"/transport/seal/register?seal={seal}")

            return resp.ok
        except ConnectionError as e:
            raise APIError("Could not establish a connection to the server")    
