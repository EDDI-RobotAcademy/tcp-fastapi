import json
import queue

from llama_test.repository.llama_test_repository import LlamaTestRepository


class LlamaTestRepositoryImpl(LlamaTestRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"LlamaTestRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
