import os
import sys

from llama_three_test.repository.llama_three_test_repository_impl import LlamaThreeTestRepositoryImpl
from llama_three_test.service.llama_three_test_service import LlamaThreeTestService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

class LlamaThreeTestServiceImpl(LlamaThreeTestService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__llamaThreeTestRepository = LlamaThreeTestRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestLlamaThreeTestResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__llamaThreeTestRepository.getResult(userDefinedReceiverFastAPIChannel)

    