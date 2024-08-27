from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from openai_api_test.service.openai_api_test_service_impl import OpenaiApiTestServiceImpl
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

openaiApiTestRouter = APIRouter()

async def injectOpenaiApiTestService() -> OpenaiApiTestServiceImpl:
    return OpenaiApiTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@openaiApiTestRouter.get("/openai-api-test-result")
async def ChatWithOpenaiApi(openaiApiTestService: OpenaiApiTestServiceImpl =
                            Depends(injectOpenaiApiTestService)):
    ColorPrinter.print_important_message("requestLlamaThreeTestResult()")

    generatedText = await openaiApiTestService.letsChat()

    return JSONResponse(content=generatedText, status_code=status.HTTP_200_OK)
