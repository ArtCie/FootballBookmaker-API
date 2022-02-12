from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def handle(self, handlers, repositories, local_rounds, current_rounds, cursor):
        pass