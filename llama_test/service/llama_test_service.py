from abc import ABC, abstractmethod


class LlamaTestService(ABC):
    @abstractmethod
    def requestLlamaTestResult(self):
        pass
