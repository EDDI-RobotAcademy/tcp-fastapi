from abc import ABC, abstractmethod


class OpenaiApiTestService(ABC):
    @abstractmethod
    def letsChat(self, userSendMessage):
        pass