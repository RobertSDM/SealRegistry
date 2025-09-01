import aiohttp

from app.constants import API_ENDPOINT
from app.exceptions import AppError
from ..interfaces.seal_api_interface import SealAPI
from aiohttp.client_exceptions import ClientConnectorError


class HTTPSealAPI(SealAPI):
    @staticmethod
    async def validate(seal: int):
        try:
            url = f"/transport/seal/check?seal={seal}"

            async with aiohttp.ClientSession(API_ENDPOINT) as session:
                async with session.get(url) as resp:
                    return resp.ok
        except ClientConnectorError as e:
            raise AppError("Could not establish a connection to the server")

    @staticmethod
    async def register(seal: int) -> bool:
        try:
            url = f"/transport/seal/register?seal={seal}"

            async with aiohttp.ClientSession(API_ENDPOINT) as session:
                async with session.post(url) as resp:
                    return resp.ok
        except ClientConnectorError as e:
            raise AppError("Could not establish a connection to the server")
