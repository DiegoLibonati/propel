import logging

from pytest import raises

from src.models.Task import Task
from src.models.TaskManager import TaskManager
from src.utils.exceptions import InvalidTaskError
from src.utils.exceptions import TaskAlreadyExistsError
from src.utils.exceptions import InvalidTaskIdError
from src.utils.exceptions import TaskNotFoundError


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_add_task(task_manager: TaskManager, task: Task, task2: Task) -> None:
    task_manager.add_task(task=task)
    task_manager.add_task(task=task2)

    len_task_manager = len(task_manager.tasks)

    assert task.id in task_manager.tasks_keys
    assert task2.id in task_manager.tasks_keys
    assert len_task_manager == task_manager.len_tasks

def test_add_task_invalid_task(task_manager: TaskManager) -> None:
    wrong_task = {
        "pepe": 1234
    }

    with raises(InvalidTaskError) as exc_info:
        task_manager.add_task(task=wrong_task)

    assert str(exc_info.value) == "You must enter a valid Task template."

def test_add_task_already_exists(task_manager: TaskManager, task: Task) -> None:
    with raises(TaskAlreadyExistsError) as exc_info:
        task_manager.add_task(task=task)
        task_manager.add_task(task=task)

    assert str(exc_info.value) == "This task already exists in the task list."

def test_remove_task(task_manager: TaskManager, task: Task, task2: Task) -> None:
    task_manager.add_task(task=task)
    task_manager.add_task(task=task2)

    len_task_manager = task_manager.len_tasks

    task_manager.remove_task(id_task=task.id)
    
    assert task_manager.len_tasks == len_task_manager - 1
    assert not task.id in task_manager.tasks_keys

def test_remove_task_invalid_idtask(task_manager: TaskManager) -> None:
    wrong_task_id = ""

    with raises(InvalidTaskIdError) as exc_info:
        task_manager.remove_task(id_task=wrong_task_id)

    assert str(exc_info.value) == "You must enter a valid ID."

def test_edit_task(task_manager: TaskManager, task: Task) -> None:
    new_title_task = "Pepe"

    task_manager.add_task(task=task)
    task_manager.edit_task(id_task=task.id, title=new_title_task)

    assert task.title == new_title_task

def test_edit_task_invalid_idtask(task_manager: TaskManager) -> None:
    new_title_task = "Pepe"
    wrong_task_id = ""

    with raises(InvalidTaskIdError) as exc_info:
        task_manager.edit_task(id_task=wrong_task_id, title=new_title_task)

    assert str(exc_info.value) == "You must enter a valid ID."

def test_move_task_by_state(task_manager: TaskManager, task: Task) -> None:
    task_manager.add_task(task=task)
    task_manager.move_task_by_state(id_task=task.id, state="in_progress")

    assert task.state == "in_progress"

def test_move_task_by_state_invalid_idtask(task_manager: TaskManager) -> None:
    wrong_task_id = ""

    with raises(InvalidTaskIdError) as exc_info:
        task_manager.move_task_by_state(id_task=wrong_task_id, state="in_progress")

    assert str(exc_info.value) == "You must enter a valid ID."

def test_not_find_task_by_idtask(task_manager: TaskManager, task: Task, task2: Task) -> None:
    wrong_idtask_to_find = "asd123"

    task_manager.add_task(task=task)
    task_manager.add_task(task=task2)

    with raises(TaskNotFoundError) as exc_info:
        task_manager.edit_task(id_task=wrong_idtask_to_find, title="Pepe")

    assert str(exc_info.value) == f"Task not found."
