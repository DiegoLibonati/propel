from datetime import datetime

from src.models.Task import Task
from src.models.Task import StateType
from src.utils.exceptions import InvalidTaskIdError
from src.utils.exceptions import TaskNotFoundError
from src.utils.exceptions import InvalidTaskError
from src.utils.exceptions import TaskAlreadyExistsError


class TaskManager:
    def __init__(self) -> None:
        self.__tasks: list[Task] = []

    @property
    def tasks(self) -> list[Task]:
        return self.__tasks

    def add_task(self, task: Task) -> None:
        if not isinstance(task, Task): raise InvalidTaskError("You must enter a valid Task template.")
        
        if task in self.tasks: raise TaskAlreadyExistsError("This task already exists in the task list")

        self.__tasks.append(task)

    def remove_task(self, id_task: str) -> None:
        if not id_task: raise InvalidTaskIdError("You must enter a valid ID.")

        self.__tasks = [task for task in self.tasks if task.id != id_task]

    def edit_task(self, id_task: str, title: str = "", description: str = "", expiration_date: datetime = None) -> None:
        if not id_task: raise InvalidTaskIdError("You must enter a valid ID.")
        
        self.current_task = self._find_task_by_id(id_task=id_task)
        self.current_task.edit(title=title, description=description, expiration_date=expiration_date)

    def move_task_by_state(self, id_task: str, state: StateType) -> None:
        if not id_task: raise InvalidTaskIdError("You must enter a valid ID.")
        
        self.current_task = self._find_task_by_id(id_task=id_task)
        self.current_task.change_task_state(state=state)

    def print_tasks(self) -> None:
        print(f"----- Tasks ({len(self.tasks)}) -----")
        for task in self.tasks:
            print(f"---- Start Task: {task.id} -----")
            print(task)
            print(f"---- End Task: {task.id} -----")

    def _find_task_by_id(self, id_task: str) -> Task:
        for task in self.tasks:
            if task.id == id_task:
                return task
        raise TaskNotFoundError(f"Task not found.")

def main() -> None:
    task_manager = TaskManager()
    
    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24)
    )

    task2 = Task(
        title="Tarea 2",
        description="Esta es una descripcion de la tarea 2",
        expiration_date=datetime(year=2025, month=2, day=24)
    )

    task_manager.add_task(task=task)
    task_manager.add_task(task=task2)

    task_manager.print_tasks()


if __name__ == "__main__":
    main()