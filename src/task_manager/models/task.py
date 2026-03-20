from datetime import datetime
from uuid import uuid4

from task_manager.configs.logger_config import setup_logger
from task_manager.constants.codes import CODE_NOT_VALID_PROPERTIES_TASK, CODE_NOT_VALID_STATUS_TASK
from task_manager.constants.messages import MESSAGE_NOT_VALID_PROPERTIES_TASK, MESSAGE_NOT_VALID_STATUS_TASK
from task_manager.constants.types import StateType
from task_manager.constants.vars import States
from task_manager.utils.exceptions import ValidationError

logger = setup_logger("Task Manager - task.py")


class Task:
    def __init__(
        self,
        title: str,
        description: str,
        expiration_date: datetime,
        state: StateType = "pending",
    ) -> None:
        self.__id = uuid4()
        self._title = title
        self._description = description
        self._expiration_date = expiration_date
        self.__state = state

    @property
    def id(self) -> str:
        return self.__id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def expiration_date(self) -> str:
        return self._expiration_date

    @property
    def state(self) -> str:
        return self.__state

    def change_state(self, state: StateType) -> None:
        if state not in States:
            raise ValidationError(code=CODE_NOT_VALID_STATUS_TASK, message=MESSAGE_NOT_VALID_STATUS_TASK)

        previous_state = self.state
        self.__state = state
        logger.info(f"{self._title} task with {previous_state} status was changed to {state}")

    def edit(self, title: str = "", description: str = "", expiration_date: datetime = None) -> None:
        if not title and not description and not expiration_date:
            raise ValidationError(code=CODE_NOT_VALID_PROPERTIES_TASK, message=MESSAGE_NOT_VALID_PROPERTIES_TASK)

        dict = {
            "_title": title,
            "_description": description,
            "_expiration_date": expiration_date,
        }

        for key, value in dict.items():
            if value:
                setattr(self, key, value)

    def __str__(self) -> None:
        return f"Task: {self.id}\nTitle: {self._title}\nDescription: {self._description}\nExpiration Date: {self._expiration_date}\nState: {self.state}"


def main() -> None:
    logger.info("----- Main Task.py -----")

    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24),
    )

    logger.info(task)

    task.change_state(state="in_progress")

    logger.info(task)


if __name__ == "__main__":
    main()
