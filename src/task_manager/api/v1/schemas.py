import uuid
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    CREATED = "создано"
    IN_PROGRESS = "в работе"
    COMPLETED = "завершено"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название задачи")
    description: Optional[str] = Field(
        None, max_length=500, description="Описание задачи"
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[TaskStatus] = None


class TaskInDB(TaskBase):
    uuid: uuid.UUID
    status: TaskStatus

    class Config:
        from_attributes = True
