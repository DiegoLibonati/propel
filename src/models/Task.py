from datetime import datetime
from typing import Literal
from uuid import uuid4

from src.utils.exceptions import InvalidTaskStateError
from src.utils.exceptions import InvalidTaskEdit

StateType = Literal["pending", "in_progress", "complete"] 
States = ["pending", "in_progress", "complete"]

class Task:
    def __init__(
        self, title: str, description: str, 
        expiration_date: datetime, state: StateType = "pending"
    ) -> None:
        self.__id = uuid4()
        self.title = title
        self.description = description
        self.expiration_date = expiration_date
        self.__state = state

    @property
    def id(self) -> str:
        return self.__id
    
    @property 
    def state(self) -> str:
        return self.__state

    def change_task_state(self, state: StateType) -> None:
        if not state in States: raise InvalidTaskStateError("You must enter a valid status to change the status of a task.")
        
        previous_state = self.state
        self.__state = state
        print(f"{self.title} task with {previous_state} status was changed to {state}")

    def edit(self, title: str = "", description: str = "", expiration_date: datetime = None) -> None:
        if not title and not description and not expiration_date: raise InvalidTaskEdit("You must send at least one param to edit a task.")

        dict = {
            "title": title,
            "description": description,
            "expiration_date": expiration_date
        }

        for key, value in dict.items():
            if value:
                setattr(self, key, value)
    
    def __str__(self) -> None:
        return (
            f"Task: {self.id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Expiration Date: {self.expiration_date}\n"
            f"State: {self.state}"
        )


def main() -> None:
    print("----- Main Task.py -----")

    task = Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=datetime(year=2025, month=2, day=24)
    )

    print(task)

    task.change_task_state(state="in_progress")


if __name__ == "__main__":
    main()