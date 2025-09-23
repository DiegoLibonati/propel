from datetime import datetime
from typing import Literal
from uuid import uuid4

from src.utils.exceptions import InvalidTaskEdit, InvalidTaskStateError

StateType = Literal["pending", "in_progress", "complete"]
States = ["pending", "in_progress", "complete"]


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
            raise InvalidTaskStateError(
                "You must enter a valid status to change the status of a task."
            )

        previous_state = self.state
        self.__state = state
        print(f"{self._title} task with {previous_state} status was changed to {state}")

    def edit(
        self, title: str = "", description: str = "", expiration_date: datetime = None
    ) -> None:
        if not title and not description and not expiration_date:
            raise InvalidTaskEdit("You must send at least one param to edit a task.")

        dict = {
            "_title": title,
            "_description": description,
            "_expiration_date": expiration_date,
        }

        for key, value in dict.items():
            if value:
                setattr(self, key, value)

    def __str__(self) -> None:
        return (
            f"Task: {self.id}\n"
            f"Title: {self._title}\n"
            f"Description: {self._description}\n"
            f"Expiration Date: {self._expiration_date}\n"
            f"State: {self.state}"
        )


def main() -> None:
    print("----- Main Task.py -----")

    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24),
    )

    print(task)

    task.change_task_state(state="in_progress")

    print(task)


if __name__ == "__main__":
    main()
