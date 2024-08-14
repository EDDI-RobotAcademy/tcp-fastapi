from pydantic import BaseModel


class OpenaiApiTestRequestForm(BaseModel):
    userInput: str
