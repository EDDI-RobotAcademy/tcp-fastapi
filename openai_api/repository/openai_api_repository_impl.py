import json
import queue

from openai_api.repository.openai_api_repository import OpenaiApiRepository


class OpenaiApiRepositoryImpl(OpenaiApiRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"OpenaiApiRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"
