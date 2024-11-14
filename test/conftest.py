from datetime import datetime

from pytest import fixture

from src.models.Task import Task
from src.models.TaskManager import TaskManager


EXPIRATION_DATE_TASK = datetime(year=2025, month=2, day=24)


@fixture
def task() -> Task:
    return Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=EXPIRATION_DATE_TASK
    )


@fixture
def task2() -> Task:
    return Task(
        title="Tarea 2",
        description="Esta es una descripcion de la tarea 2",
        expiration_date=EXPIRATION_DATE_TASK
    )


@fixture
def task_manager() -> TaskManager:
    return TaskManager()