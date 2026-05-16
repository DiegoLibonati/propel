from datetime import datetime
from uuid import UUID

import pytest

from propel.models.task_model import TaskModel
from propel.utils.exceptions import ValidationError


class TestTaskModelInit:
    @pytest.mark.unit
    def test_default_state_is_pending(self) -> None:
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=datetime(2026, 12, 31),
        )
        assert task.state == "pending"

    @pytest.mark.unit
    def test_custom_state_on_init(self) -> None:
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=datetime(2026, 12, 31),
            state="in_progress",
        )
        assert task.state == "in_progress"

    @pytest.mark.unit
    def test_title_stored_correctly(self) -> None:
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=datetime(2026, 12, 31),
        )
        assert task.title == "My Task"

    @pytest.mark.unit
    def test_description_stored_correctly(self) -> None:
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=datetime(2026, 12, 31),
        )
        assert task.description == "My Description"

    @pytest.mark.unit
    def test_expiration_date_stored_correctly(self) -> None:
        expiration: datetime = datetime(2026, 12, 31)
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=expiration,
        )
        assert task.expiration_date == expiration

    @pytest.mark.unit
    def test_id_is_uuid(self) -> None:
        task: TaskModel = TaskModel(
            title="My Task",
            description="My Description",
            expiration_date=datetime(2026, 12, 31),
        )
        assert isinstance(task.id, str)
        assert UUID(task.id).version == 4

    @pytest.mark.unit
    def test_each_instance_has_unique_id(self) -> None:
        task1: TaskModel = TaskModel(
            title="Task 1",
            description="Desc 1",
            expiration_date=datetime(2026, 12, 31),
        )
        task2: TaskModel = TaskModel(
            title="Task 2",
            description="Desc 2",
            expiration_date=datetime(2026, 12, 31),
        )
        assert task1.id != task2.id


class TestTaskModelChangeState:
    @pytest.mark.unit
    def test_change_state_to_in_progress(self, task: TaskModel) -> None:
        task.change_state(state="in_progress")
        assert task.state == "in_progress"

    @pytest.mark.unit
    def test_change_state_to_complete(self, task: TaskModel) -> None:
        task.change_state(state="complete")
        assert task.state == "complete"

    @pytest.mark.unit
    def test_change_state_to_pending(self, task: TaskModel) -> None:
        task.change_state(state="in_progress")
        task.change_state(state="pending")
        assert task.state == "pending"

    @pytest.mark.unit
    def test_change_state_invalid_raises_validation_error(self, task: TaskModel) -> None:
        with pytest.raises(ValidationError):
            task.change_state(state="invalid_state")

    @pytest.mark.unit
    def test_change_state_empty_string_raises_validation_error(self, task: TaskModel) -> None:
        with pytest.raises(ValidationError):
            task.change_state(state="")

    @pytest.mark.unit
    def test_change_state_error_has_correct_code(self, task: TaskModel) -> None:
        with pytest.raises(ValidationError) as exc_info:
            task.change_state(state="wrong")
        assert exc_info.value.code == "NOT_VALID_STATUS_TASK"


class TestTaskModelEdit:
    @pytest.mark.unit
    def test_edit_title_only(self, task: TaskModel) -> None:
        task.edit(title="New Title")
        assert task.title == "New Title"

    @pytest.mark.unit
    def test_edit_description_only(self, task: TaskModel) -> None:
        task.edit(description="New Description")
        assert task.description == "New Description"

    @pytest.mark.unit
    def test_edit_expiration_date_only(self, task: TaskModel) -> None:
        new_date: datetime = datetime(2027, 6, 15)
        task.edit(expiration_date=new_date)
        assert task.expiration_date == new_date

    @pytest.mark.unit
    def test_edit_multiple_fields(self, task: TaskModel) -> None:
        new_date: datetime = datetime(2027, 6, 15)
        task.edit(title="Updated", description="Updated Desc", expiration_date=new_date)
        assert task.title == "Updated"
        assert task.description == "Updated Desc"
        assert task.expiration_date == new_date

    @pytest.mark.unit
    def test_edit_no_fields_raises_validation_error(self, task: TaskModel) -> None:
        with pytest.raises(ValidationError):
            task.edit()

    @pytest.mark.unit
    def test_edit_no_fields_error_has_correct_code(self, task: TaskModel) -> None:
        with pytest.raises(ValidationError) as exc_info:
            task.edit()
        assert exc_info.value.code == "NOT_VALID_PROPERTIES_TASK"

    @pytest.mark.unit
    def test_edit_does_not_change_untouched_fields(self, task: TaskModel) -> None:
        original_description: str = task.description
        original_date: datetime = task.expiration_date
        task.edit(title="Only Title Changed")
        assert task.description == original_description
        assert task.expiration_date == original_date

    @pytest.mark.unit
    def test_edit_does_not_change_id(self, task: TaskModel) -> None:
        original_id: str = task.id
        task.edit(title="Changed")
        assert task.id == original_id

    @pytest.mark.unit
    def test_edit_does_not_change_state(self, task: TaskModel) -> None:
        task.change_state(state="in_progress")
        task.edit(title="Changed")
        assert task.state == "in_progress"


class TestTaskModelStr:
    @pytest.mark.unit
    def test_str_contains_title(self, task: TaskModel) -> None:
        result: str = str(task)
        assert "Test Task" in result

    @pytest.mark.unit
    def test_str_contains_description(self, task: TaskModel) -> None:
        result: str = str(task)
        assert "Test Description" in result

    @pytest.mark.unit
    def test_str_contains_state(self, task: TaskModel) -> None:
        result: str = str(task)
        assert "pending" in result
