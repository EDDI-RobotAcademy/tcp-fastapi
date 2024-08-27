import os
import sys

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

from openai_api_test.repository.openai_api_test_repository_impl import OpenaiApiTestRepositoryImpl
from openai_api_test.service.openai_api_test_service import OpenaiApiTestService


class OpenaiApiTestServiceImpl(OpenaiApiTestService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__openaiApiTestRepository = OpenaiApiTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def letsChat(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return await self.__openaiApiTestRepository.generateText(userDefinedReceiverFastAPIChannel)