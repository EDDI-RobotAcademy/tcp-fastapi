from abc import ABC, abstractmethod


class OpenaiApiRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass