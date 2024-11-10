import logging

from datetime import datetime

from pytest import fixture
from pytest import raises

from src.models.Task import Task
from src.utils.exceptions import InvalidTaskStateError
from src.utils.exceptions import InvalidTaskEdit


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

EXPIRATION_DATE_TASK = datetime(year=2025, month=2, day=24)


@fixture
def task() -> Task:
    return Task(
        title="Tarea 1",
        description="Esta es una descripcion de la tarea",
        expiration_date=EXPIRATION_DATE_TASK
    )


def test_create_task(task: Task) -> None:
    assert task.title == "Tarea 1"
    assert task.description == "Esta es una descripcion de la tarea"
    assert task.expiration_date == EXPIRATION_DATE_TASK
    assert task.state == "pending"


def test_change_state(task: Task) -> None:
    task.change_task_state("in_progress")
    
    assert task.state == "in_progress"


def test_change_state_invalid_task_state(task: Task) -> None:    
    with raises(InvalidTaskStateError) as exc_info:
        task.change_task_state(state="asd")

    assert str(exc_info.value) == "You must enter a valid status to change the status of a task."

    
def test_edit_task(task: Task) -> None:
    new_title = "Tarea Editada 1"
    new_description = "Descripcion Editada"
    new_expiration_date = datetime(year=2025, month=2, day=25)

    task.edit(title=new_title, description=new_description, expiration_date=new_expiration_date)

    assert task.title == new_title
    assert task.description == new_description
    assert task.expiration_date == new_expiration_date


def test_edit_only_title_task(task: Task) -> None:
    new_title = "Tarea Editada 1"

    task.edit(title=new_title)

    assert task.title == new_title
    assert task.description == task.description
    assert task.expiration_date == task.expiration_date


def test_edit_invalid_task(task: Task) -> None:
    with raises(InvalidTaskEdit) as exc_info:
        task.edit()

    assert str(exc_info.value) == "You must send at least one param to edit a task."
