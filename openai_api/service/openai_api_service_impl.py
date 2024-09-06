import os
import sys

from openai_api.repository.openai_api_repository_impl import OpenaiApiRepositoryImpl
from openai_api.service.openai_api_service import OpenaiApiService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class OpenaiApiServiceImpl(OpenaiApiService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__openaiApiRepository = OpenaiApiRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestOpenaiApiResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__openaiApiRepository.getResult(userDefinedReceiverFastAPIChannel)
