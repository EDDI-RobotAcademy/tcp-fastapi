import json
import queue

from llama_three_test.repository.llama_three_test_repository import LlamaThreeTestRepository


class LlamaThreeTestRepositoryImpl(LlamaThreeTestRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"LlamaThreeTestRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
