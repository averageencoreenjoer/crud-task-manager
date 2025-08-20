import uuid
from typing import List
from ..api.v1 import schemas
from ..db import storage
from ..core.exceptions import TaskNotFoundException


def create(task_in: schemas.TaskCreate) -> schemas.TaskInDB:
    new_uuid = uuid.uuid4()
    task = schemas.TaskInDB(
        uuid=new_uuid,
        title=task_in.title,
        description=task_in.description,
        status=schemas.TaskStatus.CREATED,
    )
    storage.db[new_uuid] = task
    return task


def get(task_uuid: uuid.UUID) -> schemas.TaskInDB:
    task = storage.db.get(task_uuid)
    if not task:
        raise TaskNotFoundException
    return task


def get_all() -> List[schemas.TaskInDB]:
    return list(storage.db.values())


def update(task_uuid: uuid.UUID, task_in: schemas.TaskUpdate) -> schemas.TaskInDB:
    task = storage.db.get(task_uuid)
    if not task:
        raise TaskNotFoundException

    update_data = task_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    storage.db[task_uuid] = task
    return task


def delete(task_uuid: uuid.UUID) -> None:
    if task_uuid not in storage.db:
        raise TaskNotFoundException
    del storage.db[task_uuid]
