from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from openai_api_test.controller.request_form.openai_api_test_request_form import OpenaiApiTestRequestForm
from openai_api_test.service.openai_api_test_service_impl import OpenaiApiTestServiceImpl

openaiApiTestRouter = APIRouter()

async def injectOpenaiApiTestService() -> OpenaiApiTestServiceImpl:
    return OpenaiApiTestServiceImpl()

@openaiApiTestRouter.post("/openai-api-test")
async def ChatWithOpenaiApi(openaiApiTestRequestForm: OpenaiApiTestRequestForm,
                            openaiApiTestService: OpenaiApiTestServiceImpl =
                            Depends(injectOpenaiApiTestService)):
    print(f"controller -> ChatWithOpenaiApi():\n"
          f"OpenaiApiTestRequestForm: {openaiApiTestRequestForm.userInput}")

    generatedText = await openaiApiTestService.letsChat(openaiApiTestRequestForm.userInput)

    return JSONResponse(content=generatedText, status_code=status.HTTP_200_OK)
