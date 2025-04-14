from pydantic import BaseModel, Field
from docs.tasks_docs import task_fields, task_example
from typing import Optional, List

class TaskCreate(BaseModel):
    title: str = Field(..., description=task_fields["title"])
    description: Optional[str] = Field(None, description=task_fields["description"])
    completed: bool = Field(default=False, description=task_fields["completed"])

    class Config:
        schema_extra = {"example": task_example}