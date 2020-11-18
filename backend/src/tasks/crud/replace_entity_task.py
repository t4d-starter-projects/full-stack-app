from typing import TypeVar, Generic

from src.core.interfaces.logging import LoggingInterface
from src.core.interfaces.crud import CRUDInterface
from ..task_interface import TaskInterface

EntityType = TypeVar('EntityType')


class ReplaceEntityTask(TaskInterface[EntityType], Generic[EntityType]):

    def __init__(self, logging: LoggingInterface,
                 entities: CRUDInterface[EntityType]):
        self.logging = logging
        self.entities = entities

    def run(self, entity_id):
        return self.entities.replace_one(entity_id)
