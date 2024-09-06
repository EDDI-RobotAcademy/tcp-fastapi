import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from openai_api.service.openai_api_service_impl import OpenaiApiServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


openaiApiRouter = APIRouter()

async def injectOpenaiApiService() -> OpenaiApiServiceImpl:
    return OpenaiApiServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@openaiApiRouter.get('/openai-api-result')
async def requestOpenaiApiResult(oepnaiApiService: OpenaiApiServiceImpl =
                                 Depends(injectOpenaiApiService)):

    ColorPrinter.print_important_message("requestOpenaiApiResult()")

    generatedOpenaiApiResult = oepnaiApiService.requestOpenaiApiResult()

    return JSONResponse(content=generatedOpenaiApiResult, status_code=status.HTTP_200_OK)
