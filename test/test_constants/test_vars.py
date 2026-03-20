from task_manager.constants.vars import States


class TestStatesValues:
    def test_contains_pending(self) -> None:
        assert "pending" in States

    def test_contains_in_progress(self) -> None:
        assert "in_progress" in States

    def test_contains_complete(self) -> None:
        assert "complete" in States


class TestStatesStructure:
    def test_is_list(self) -> None:
        assert isinstance(States, list)

    def test_has_exactly_three_elements(self) -> None:
        assert len(States) == 3

    def test_all_elements_are_strings(self) -> None:
        for state in States:
            assert isinstance(state, str)
