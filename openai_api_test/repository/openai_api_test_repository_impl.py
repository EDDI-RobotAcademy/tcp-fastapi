import json
import queue

from openai_api_test.repository.openai_api_test_repository import OpenaiApiTestRepository



class OpenaiApiTestRepositoryImpl(OpenaiApiTestRepository):
    async def generateText(self, userDefinedReceiverFastAPIChannel):
        print(f"LlamaThreeTestRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"


        