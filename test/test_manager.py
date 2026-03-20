from collections.abc import KeysView, ValuesView
from datetime import datetime

import pytest

from task_manager.constants.codes import (
    CODE_ALREADY_EXISTS_TASK,
    CODE_NOT_FOUND_TASK,
    CODE_NOT_VALID_PROPERTIES_TASK,
    CODE_NOT_VALID_TASK,
)
from task_manager.manager import Manager
from task_manager.models.task import Task
from task_manager.utils.exceptions import ConflictError, NotFoundError, ValidationError


class TestManagerInit:
    def test_tasks_is_empty_on_init(self, manager: Manager) -> None:
        assert manager.tasks == {}

    def test_len_tasks_is_zero_on_init(self, manager: Manager) -> None:
        assert manager.len_tasks == 0

    def test_tasks_is_dict(self, manager: Manager) -> None:
        assert isinstance(manager.tasks, dict)


class TestManagerProperties:
    def test_tasks_keys_returns_keys_view(self, manager_with_task: Manager) -> None:
        assert isinstance(manager_with_task.tasks_keys, KeysView)

    def test_tasks_values_returns_values_view(self, manager_with_task: Manager) -> None:
        assert isinstance(manager_with_task.tasks_values, ValuesView)

    def test_len_tasks_matches_task_count(self, manager_with_task: Manager) -> None:
        assert manager_with_task.len_tasks == 1

    def test_tasks_keys_contains_task_id(self, manager_with_task: Manager, task: Task) -> None:
        assert task.id in manager_with_task.tasks_keys

    def test_tasks_values_contains_task(self, manager_with_task: Manager, task: Task) -> None:
        assert task in manager_with_task.tasks_values


class TestManagerAddTask:
    def test_add_task_increases_len(self, manager: Manager, task: Task) -> None:
        manager.add_task(task=task)
        assert manager.len_tasks == 1

    def test_add_task_stores_task_in_values(self, manager: Manager, task: Task) -> None:
        manager.add_task(task=task)
        assert task in manager.tasks_values

    def test_add_task_stores_task_by_id_key(self, manager: Manager, task: Task) -> None:
        manager.add_task(task=task)
        assert task.id in manager.tasks_keys

    def test_add_multiple_tasks(self, manager: Manager, expiration_date: datetime) -> None:
        task_a = Task(title="A", description="A", expiration_date=expiration_date)
        task_b = Task(title="B", description="B", expiration_date=expiration_date)
        manager.add_task(task=task_a)
        manager.add_task(task=task_b)
        assert manager.len_tasks == 2

    def test_add_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_task(task="not a task")

    def test_add_invalid_type_error_code(self, manager: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager.add_task(task="not a task")
        assert exc_info.value.code == CODE_NOT_VALID_TASK

    def test_add_duplicate_task_raises_conflict_error(self, manager: Manager, task: Task) -> None:
        manager.add_task(task=task)
        with pytest.raises(ConflictError):
            manager.add_task(task=task)

    def test_add_duplicate_task_error_code(self, manager: Manager, task: Task) -> None:
        manager.add_task(task=task)
        with pytest.raises(ConflictError) as exc_info:
            manager.add_task(task=task)
        assert exc_info.value.code == CODE_ALREADY_EXISTS_TASK


class TestManagerRemoveTask:
    def test_remove_task_decreases_len(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.remove_task(id_task=task.id)
        assert manager_with_task.len_tasks == 0

    def test_remove_task_not_in_values(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.remove_task(id_task=task.id)
        assert task not in manager_with_task.tasks_values

    def test_remove_task_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.remove_task(id_task="")

    def test_remove_task_empty_id_error_code(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager_with_task.remove_task(id_task="")
        assert exc_info.value.code == CODE_NOT_VALID_PROPERTIES_TASK

    def test_remove_task_not_found_raises_not_found_error(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError):
            manager.remove_task(id_task=task.id)

    def test_remove_task_not_found_error_code(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            manager.remove_task(id_task=task.id)
        assert exc_info.value.code == CODE_NOT_FOUND_TASK


class TestManagerEditTask:
    def test_edit_task_title(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.edit_task(id_task=task.id, title="New Title")
        assert task.title == "New Title"

    def test_edit_task_description(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.edit_task(id_task=task.id, description="New Description")
        assert task.description == "New Description"

    def test_edit_task_expiration_date(self, manager_with_task: Manager, task: Task) -> None:
        new_date = datetime(year=2026, month=6, day=15)
        manager_with_task.edit_task(id_task=task.id, expiration_date=new_date)
        assert task.expiration_date == new_date

    def test_edit_task_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.edit_task(id_task="")

    def test_edit_task_empty_id_error_code(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager_with_task.edit_task(id_task="")
        assert exc_info.value.code == CODE_NOT_VALID_PROPERTIES_TASK

    def test_edit_task_not_found_raises_not_found_error(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError):
            manager.edit_task(id_task=task.id, title="X")

    def test_edit_task_no_properties_raises_validation_error(self, manager_with_task: Manager, task: Task) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.edit_task(id_task=task.id)


class TestManagerMoveTaskByState:
    def test_move_task_changes_state(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.move_task_by_state(id_task=task.id, state="in_progress")
        assert task.state == "in_progress"

    def test_move_task_to_complete(self, manager_with_task: Manager, task: Task) -> None:
        manager_with_task.move_task_by_state(id_task=task.id, state="complete")
        assert task.state == "complete"

    def test_move_task_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.move_task_by_state(id_task="", state="in_progress")

    def test_move_task_empty_id_error_code(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager_with_task.move_task_by_state(id_task="", state="in_progress")
        assert exc_info.value.code == CODE_NOT_VALID_PROPERTIES_TASK

    def test_move_task_not_found_raises_not_found_error(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError):
            manager.move_task_by_state(id_task=task.id, state="in_progress")

    def test_move_task_invalid_state_raises_validation_error(self, manager_with_task: Manager, task: Task) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.move_task_by_state(id_task=task.id, state="invalid")


class TestManagerFindTaskById:
    def test_find_existing_task_returns_task(self, manager_with_task: Manager, task: Task) -> None:
        found = manager_with_task._find_task_by_id(id_task=task.id)
        assert found is task

    def test_find_missing_task_raises_not_found_error(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError):
            manager._find_task_by_id(id_task=task.id)

    def test_find_missing_task_error_code(self, manager: Manager, task: Task) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            manager._find_task_by_id(id_task=task.id)
        assert exc_info.value.code == CODE_NOT_FOUND_TASK


class TestManagerLoggingTask:
    def test_logging_task_does_not_raise(self, manager_with_task: Manager) -> None:
        manager_with_task.logging_task()

    def test_logging_task_empty_manager_does_not_raise(self, manager: Manager) -> None:
        manager.logging_task()
