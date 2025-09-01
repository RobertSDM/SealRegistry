from abc import ABC, abstractmethod


class SealAPI(ABC):
    @abstractmethod
    async def validate(seal: int) -> bool:
        """
        Validade if the seal is registered or not

        Args
        ---
        seal
            The seal to be validated
        
        Returns
        ---
        If the seal is valid or not
        """

        pass

    @abstractmethod
    async def register(seal: int) -> bool:
        """
        Register the seal

        Args
        ---
        seal
            The seal to be registered

        Returns
        ---
        If the seal was registered or not
        """

        pass
