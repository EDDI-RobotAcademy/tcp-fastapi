from abc import ABC, abstractmethod


class LlamaThreeTestService(ABC):
    @abstractmethod
    def requestLlamaThreeTestResult(self):
        pass
