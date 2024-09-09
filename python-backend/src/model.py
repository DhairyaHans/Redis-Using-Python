from pydantic import BaseModel

class RequestBody(BaseModel):
    problemId: int
    userId: int
    code: str|None
    language: str|None