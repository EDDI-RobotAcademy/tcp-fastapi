from abc import ABC, abstractmethod


class LlamaTestRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass