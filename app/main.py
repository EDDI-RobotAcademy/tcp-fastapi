import os.path
import sys
from fastapi.middleware.cors import CORSMiddleware

import colorama

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from openai_api.controller.openai_api_controller import openaiApiRouter
from user_defined_initializer.init import UserDefinedInitializer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.deep_learning.controller.deep_learning_controller import deepLearningRouter
from template.dice.controller.dice_controller import diceResultRouter
from template.system_initializer.init import SystemInitializer
from template.task_manager.manager import TaskManager
from template.include.socket_server.initializer.init_domain import DomainInitializer

DomainInitializer.initEachDomain()
SystemInitializer.initSystemDomain()
UserDefinedInitializer.initUserDefinedDomain()

app = FastAPI()

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(deepLearningRouter)
app.include_router(diceResultRouter)

app.include_router(openaiApiRouter)

if __name__ == "__main__":
    colorama.init(autoreset=True)

    TaskManager.createSocketServer()
    uvicorn.run(app, host=os.getenv('HOST'), port=int(os.getenv('FASTAPI_PORT')))
