from datetime import datetime
from uuid import UUID

import pytest

from task_manager.constants.codes import CODE_NOT_VALID_PROPERTIES_TASK, CODE_NOT_VALID_STATUS_TASK
from task_manager.models.task import Task
from task_manager.utils.exceptions import ValidationError


class TestTaskInit:
    def test_id_is_uuid(self, task: Task) -> None:
        assert isinstance(task.id, UUID)

    def test_each_task_has_unique_id(self, expiration_date: datetime) -> None:
        task_a = Task(title="A", description="A", expiration_date=expiration_date)
        task_b = Task(title="B", description="B", expiration_date=expiration_date)
        assert task_a.id != task_b.id

    def test_title_matches(self, task: Task) -> None:
        assert task.title == "Test Task"

    def test_description_matches(self, task: Task) -> None:
        assert task.description == "Test Description"

    def test_expiration_date_matches(self, task: Task, expiration_date: datetime) -> None:
        assert task.expiration_date == expiration_date

    def test_default_state_is_pending(self, task: Task) -> None:
        assert task.state == "pending"

    def test_custom_initial_state(self, expiration_date: datetime) -> None:
        task = Task(title="T", description="D", expiration_date=expiration_date, state="in_progress")
        assert task.state == "in_progress"


class TestTaskChangeState:
    def test_change_to_in_progress(self, task: Task) -> None:
        task.change_state(state="in_progress")
        assert task.state == "in_progress"

    def test_change_to_complete(self, task: Task) -> None:
        task.change_state(state="complete")
        assert task.state == "complete"

    def test_change_back_to_pending(self, task: Task) -> None:
        task.change_state(state="in_progress")
        task.change_state(state="pending")
        assert task.state == "pending"

    def test_invalid_state_raises_validation_error(self, task: Task) -> None:
        with pytest.raises(ValidationError):
            task.change_state(state="invalid_state")

    def test_invalid_state_error_code(self, task: Task) -> None:
        with pytest.raises(ValidationError) as exc_info:
            task.change_state(state="invalid_state")
        assert exc_info.value.code == CODE_NOT_VALID_STATUS_TASK

    def test_empty_state_raises_validation_error(self, task: Task) -> None:
        with pytest.raises(ValidationError):
            task.change_state(state="")


class TestTaskEdit:
    def test_edit_title(self, task: Task) -> None:
        task.edit(title="New Title")
        assert task.title == "New Title"

    def test_edit_description(self, task: Task) -> None:
        task.edit(description="New Description")
        assert task.description == "New Description"

    def test_edit_expiration_date(self, task: Task) -> None:
        new_date = datetime(year=2026, month=6, day=15)
        task.edit(expiration_date=new_date)
        assert task.expiration_date == new_date

    def test_edit_multiple_fields(self, task: Task) -> None:
        new_date = datetime(year=2026, month=1, day=1)
        task.edit(title="Multi", description="Multi desc", expiration_date=new_date)
        assert task.title == "Multi"
        assert task.description == "Multi desc"
        assert task.expiration_date == new_date

    def test_edit_does_not_change_unset_fields(self, task: Task) -> None:
        task.edit(title="Only Title Changed")
        assert task.description == "Test Description"

    def test_edit_no_properties_raises_validation_error(self, task: Task) -> None:
        with pytest.raises(ValidationError):
            task.edit()

    def test_edit_no_properties_error_code(self, task: Task) -> None:
        with pytest.raises(ValidationError) as exc_info:
            task.edit()
        assert exc_info.value.code == CODE_NOT_VALID_PROPERTIES_TASK


class TestTaskStr:
    def test_str_contains_title(self, task: Task) -> None:
        assert "Test Task" in str(task)

    def test_str_contains_description(self, task: Task) -> None:
        assert "Test Description" in str(task)

    def test_str_contains_state(self, task: Task) -> None:
        assert "pending" in str(task)

    def test_str_returns_string(self, task: Task) -> None:
        assert isinstance(str(task), str)
