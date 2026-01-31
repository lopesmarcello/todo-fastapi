from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None 

class TodoCreate(TodoBase):
    completed: bool = False

class Todo(TodoBase):
    id: int
    completed: bool = False

    class Config:
        from_attributes = True