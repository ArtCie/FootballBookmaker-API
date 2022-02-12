from abc import ABC, abstractmethod


class IEndpoint(ABC):
    @abstractmethod
    def process_request(self, kwargs, cursor):
        pass
