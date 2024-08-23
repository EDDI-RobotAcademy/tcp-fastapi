from abc import ABC, abstractmethod


class LlamaThreeTestRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass