from abc import abstractmethod, ABC


class OpenaiApiTestRepository(ABC):
    @abstractmethod
    def generateText(self, userSendMessage):
        pass