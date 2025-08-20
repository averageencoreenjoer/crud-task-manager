import uuid
from typing import List
from fastapi import APIRouter, status, Depends
from ....api.v1 import schemas
from ....crud import task_crud


router = APIRouter()


@router.post("/", response_model=schemas.TaskInDB, status_code=status.HTTP_201_CREATED)
def create_task(task_in: schemas.TaskCreate):
    return task_crud.create(task_in=task_in)


@router.get("/", response_model=List[schemas.TaskInDB])
def get_all_tasks():
    return task_crud.get_all()


@router.get("/{task_uuid}", response_model=schemas.TaskInDB)
def get_task(task: schemas.TaskInDB = Depends(task_crud.get)):
    return task


@router.put("/{task_uuid}", response_model=schemas.TaskInDB)
def update_task(task_uuid: uuid.UUID, task_in: schemas.TaskUpdate):
    return task_crud.update(task_uuid=task_uuid, task_in=task_in)


@router.delete("/{task_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_uuid: uuid.UUID):
    task_crud.delete(task_uuid=task_uuid)
