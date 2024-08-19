import os
import sys

from llama_test.repository.llama_test_repository_impl import LlamaTestRepositoryImpl
from llama_test.service.llama_test_service import LlamaTestService

from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class LlamaTestServiceImpl(LlamaTestService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__llamaTestRepository = LlamaTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestLlamaTestResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__llamaTestRepository.getResult(userDefinedReceiverFastAPIChannel)

    