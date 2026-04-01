from pydantic import BaseModel

class TaskCreateRequest(BaseModel):
    title: str
    description: str = ""

class TaskUpdateRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None