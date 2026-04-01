from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.models.task_request import TaskCreateRequest, TaskUpdateRequest
from api.models.task_response import TaskResponse
from db import get_db
from repositories.task_repository import TaskRepository
from services.task_service import TaskService
from services.models.task_rule import TaskRule

router = APIRouter()

# Dependency to get service
def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repo = TaskRepository(db)
    rule = TaskRule()
    return TaskService(repo, rule)

# CREATE TASK
@router.post("/", response_model=TaskResponse)
def create_task(payload: TaskCreateRequest, service: TaskService = Depends(get_task_service)):
    task = service.create_task(user_id=1, title=payload.title, description=payload.description)
    return TaskResponse(
        id=task.id,
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        done=task.done
    )

# GET ALL TASKS
@router.get("/", response_model=list[TaskResponse])
def get_tasks(service: TaskService = Depends(get_task_service)):
    tasks = service.get_tasks()
    return [
        TaskResponse(
            id=t.id,
            user_id=t.user_id,
            title=t.title,
            description=t.description,
            done=t.done
        )
        for t in tasks
    ]

# UPDATE TASK (supports partial updates)
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, payload: TaskUpdateRequest, service: TaskService = Depends(get_task_service)):
    task = service.update_task(
        task_id,
        title=payload.title if payload.title is not None else None,
        description=payload.description if payload.description is not None else None,
        done=payload.done if payload.done is not None else None
    )
    if not task:
        raise HTTPException(status_code=404, detail="Not found")
    return TaskResponse(
        id=task.id,
        user_id=task.user_id,
        title=task.title,
        description=task.description,
        done=task.done
    )

# DELETE TASK
@router.delete("/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    task = service.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "deleted"}