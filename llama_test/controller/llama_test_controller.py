import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from llama_test.service.llama_test_service_impl import LlamaTestServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter

llamaTestRouter = APIRouter()

async def injectLlamaTestService() -> LlamaTestServiceImpl:
    return LlamaTestServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@llamaTestRouter.get('/llama-test-result')
async def requestLlamaTestResult(llamaTestService: LlamaTestServiceImpl =
                                 Depends(injectLlamaTestService)):

    ColorPrinter.print_important_message("requestLlamaTestResult()")

    generatedLlamaTestResult = llamaTestService.requestLlamaTestResult()

    return JSONResponse(content=generatedLlamaTestResult, status_code=status.HTTP_200_OK)
