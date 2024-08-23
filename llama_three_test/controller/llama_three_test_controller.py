import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from llama_three_test.service.llama_three_test_service_impl import LlamaThreeTestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


llamaThreeTestRouter = APIRouter()

async def injectLlamaThreeTestService() -> LlamaThreeTestServiceImpl:
    return LlamaThreeTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@llamaThreeTestRouter.get('/llama-three-test-result')
async def requestLlamaThreeTestResult(llamaThreeTestService: LlamaThreeTestServiceImpl =
                                 Depends(injectLlamaThreeTestService)):

    ColorPrinter.print_important_message("requestLlamaThreeTestResult()")

    generatedLlamaThreeTestResult = llamaThreeTestService.requestLlamaThreeTestResult()

    return JSONResponse(content=generatedLlamaThreeTestResult, status_code=status.HTTP_200_OK)
