from collections.abc import KeysView, ValuesView
from datetime import datetime

from task_manager.configs.logger_config import setup_logger
from task_manager.constants.codes import CODE_ALREADY_EXISTS_TASK, CODE_NOT_FOUND_TASK, CODE_NOT_VALID_PROPERTIES_TASK, CODE_NOT_VALID_TASK
from task_manager.constants.messages import MESSAGE_ALREADY_EXISTS_TASK, MESSAGE_NOT_FOUND_TASK, MESSAGE_NOT_VALID_PROPERTIES_TASK, MESSAGE_NOT_VALID_TASK
from task_manager.constants.types import StateType
from task_manager.models import Task
from task_manager.utils.exceptions import ConflictError, NotFoundError, ValidationError

logger = setup_logger("Task Manager - manager.py")


class Manager:
    def __init__(self) -> None:
        self.__tasks: dict[str, Task] = {}

    @property
    def tasks(self) -> dict[str, Task]:
        return self.__tasks

    @property
    def tasks_keys(self) -> KeysView[str]:
        return self.tasks.keys()

    @property
    def tasks_values(self) -> ValuesView[Task]:
        return self.tasks.values()

    @property
    def len_tasks(self) -> int:
        return len(self.tasks)

    def add_task(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise ValidationError(code=CODE_NOT_VALID_TASK, message=MESSAGE_NOT_VALID_TASK)

        if task in self.tasks_values:
            raise ConflictError(code=CODE_ALREADY_EXISTS_TASK, message=MESSAGE_ALREADY_EXISTS_TASK)

        self.__tasks[task.id] = task

    def remove_task(self, id_task: str) -> None:
        if not id_task:
            raise ValidationError(code=CODE_NOT_VALID_PROPERTIES_TASK, message=MESSAGE_NOT_VALID_PROPERTIES_TASK)

        task = self._find_task_by_id(id_task=id_task)

        del self.__tasks[task.id]

    def edit_task(
        self,
        id_task: str,
        title: str = "",
        description: str = "",
        expiration_date: datetime = None,
    ) -> None:
        if not id_task:
            raise ValidationError(code=CODE_NOT_VALID_PROPERTIES_TASK, message=MESSAGE_NOT_VALID_PROPERTIES_TASK)

        task = self._find_task_by_id(id_task=id_task)

        task.edit(title=title, description=description, expiration_date=expiration_date)

    def move_task_by_state(self, id_task: str, state: StateType) -> None:
        if not id_task:
            raise ValidationError(code=CODE_NOT_VALID_PROPERTIES_TASK, message=MESSAGE_NOT_VALID_PROPERTIES_TASK)

        task = self._find_task_by_id(id_task=id_task)
        task.change_state(state=state)

    def logging_task(self) -> None:
        logger.info(f"----- Tasks ({self.len_tasks}) -----\n")
        for task in self.tasks_values:
            logger.info(f"---- Start Task: {task.id} -----")
            logger.info(task)
            logger.info(f"---- End Task: {task.id} -----\n\n")

    def _find_task_by_id(self, id_task: str) -> Task:
        task = self.tasks.get(id_task, None)

        if not task:
            raise NotFoundError(code=CODE_NOT_FOUND_TASK, message=MESSAGE_NOT_FOUND_TASK)

        return task


def main() -> None:
    task_manager = Manager()

    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24),
    )

    task2 = Task(
        title="Tarea 2",
        description="Esta es una descripcion de la tarea 2",
        expiration_date=datetime(year=2025, month=2, day=24),
    )

    task_manager.add_task(task=task)
    task_manager.add_task(task=task2)

    task_manager.logging_task()


if __name__ == "__main__":
    main()
