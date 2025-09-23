from datetime import datetime
from typing import KeysView, ValuesView

from src.models.task_t import StateType, Task
from src.utils.exceptions import (
    InvalidTaskError,
    InvalidTaskIdError,
    TaskAlreadyExistsError,
    TaskNotFoundError,
)


class TaskManager:
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
            raise InvalidTaskError("You must enter a valid Task template.")

        if task in self.tasks_values:
            raise TaskAlreadyExistsError("This task already exists in the task list.")

        self.__tasks[task.id] = task

    def remove_task(self, id_task: str) -> None:
        if not id_task:
            raise InvalidTaskIdError("You must enter a valid ID.")

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
            raise InvalidTaskIdError("You must enter a valid ID.")

        task = self._find_task_by_id(id_task=id_task)

        task.edit(title=title, description=description, expiration_date=expiration_date)

    def move_task_by_state(self, id_task: str, state: StateType) -> None:
        if not id_task:
            raise InvalidTaskIdError("You must enter a valid ID.")

        task = self._find_task_by_id(id_task=id_task)
        task.change_state(state=state)

    def print_tasks(self) -> None:
        print(f"----- Tasks ({self.len_tasks}) -----\n")
        for task in self.tasks_values:
            print(f"---- Start Task: {task.id} -----")
            print(task)
            print(f"---- End Task: {task.id} -----\n\n")

    def _find_task_by_id(self, id_task: str) -> Task:
        task = self.tasks.get(id_task, None)

        if not task:
            raise TaskNotFoundError("Task not found.")

        return task


def main() -> None:
    task_manager = TaskManager()

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

    task_manager.print_tasks()


if __name__ == "__main__":
    main()
