import uuid
from typing import Dict
from ..api.v1.schemas import TaskInDB

db: Dict[uuid.UUID, TaskInDB] = {}


def clear_db():
    db.clear()
