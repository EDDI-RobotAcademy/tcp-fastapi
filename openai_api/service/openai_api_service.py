from abc import ABC, abstractmethod


class OpenaiApiService(ABC):
    @abstractmethod
    def requestOpenaiApiResult(self):
        pass
