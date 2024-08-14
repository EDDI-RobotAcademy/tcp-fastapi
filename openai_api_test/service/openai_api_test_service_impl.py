from openai_api_test.repository.openai_api_test_repository_impl import OpenaiApiTestRepositoryImpl
from openai_api_test.service.openai_api_test_service import OpenaiApiTestService


class OpenaiApiTestServiceImpl(OpenaiApiTestService):
    def __init__(self):
        self.__openaiApiTestRepository = OpenaiApiTestRepositoryImpl()

    async def letsChat(self, userSendMessage):
        return await self.__openaiApiTestRepository.generateText(userSendMessage)