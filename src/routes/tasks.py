from fastapi import APIRouter, Depends, status, Query
from typing import Optional, List
from fastapi.responses import JSONResponse
from auth.azure_auth import verify_azure_identity
from docs.tasks_docs import task_metadata
from schemas.task import TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"],dependencies=[Depends(verify_azure_identity)])

@router.post("/", summary=task_metadata.Create.summary, description=task_metadata.Create.description)
def create_task(task: TaskCreate):
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Task created", "task": task.dict()})

@router.get("/", summary=task_metadata.List.summary, description=task_metadata.List.description)
def list_tasks(
    completed: Optional[bool] = Query(None, description="Filter tasks by completion status"),
    title: Optional[str] = Query(None, description="Filter tasks by title"),
    limit: Optional[int] = Query(10, description="Limit the number of tasks returned"),
):
    
    tasks = [
        {"title": "Example Task", "description": "An example", "completed": False},
        {"title": "Another Task", "description": "Another example", "completed": True},
    ]

    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]
    if title:
        tasks = [task for task in tasks if title.lower() in task["title"].lower()]
    tasks = tasks[:limit]

    return {"tasks": tasks}