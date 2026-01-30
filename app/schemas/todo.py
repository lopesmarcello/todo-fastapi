from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None 

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    completed: bool = False

    class Config:
        from_attributes = True