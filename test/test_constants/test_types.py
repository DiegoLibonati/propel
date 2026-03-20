from typing import get_args

from task_manager.constants.types import StateType


class TestStateTypeValues:
    def test_pending_is_valid_state(self) -> None:
        assert "pending" in get_args(StateType)

    def test_in_progress_is_valid_state(self) -> None:
        assert "in_progress" in get_args(StateType)

    def test_complete_is_valid_state(self) -> None:
        assert "complete" in get_args(StateType)


class TestStateTypeStructure:
    def test_has_exactly_three_states(self) -> None:
        assert len(get_args(StateType)) == 3

    def test_all_states_are_strings(self) -> None:
        states: tuple[str, ...] = get_args(StateType)
        for state in states:
            assert isinstance(state, str)
