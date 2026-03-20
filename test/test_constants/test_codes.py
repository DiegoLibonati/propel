from task_manager.constants.codes import (
    CODE_ALREADY_EXISTS_TASK,
    CODE_ERROR_INTERNAL_LIBRARY,
    CODE_NOT_EXISTS_TASK,
    CODE_NOT_FOUND_TASK,
    CODE_NOT_VALID_INTEGER,
    CODE_NOT_VALID_PROPERTIES_TASK,
    CODE_NOT_VALID_STATUS_TASK,
    CODE_NOT_VALID_TASK,
)


class TestCodesValues:
    def test_code_error_internal_library(self) -> None:
        assert CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    def test_code_not_valid_integer(self) -> None:
        assert CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"

    def test_code_not_valid_status_task(self) -> None:
        assert CODE_NOT_VALID_STATUS_TASK == "NOT_VALID_STATUS_TASK"

    def test_code_not_valid_properties_task(self) -> None:
        assert CODE_NOT_VALID_PROPERTIES_TASK == "NOT_VALID_PROPERTIES_TASK"

    def test_code_not_valid_task(self) -> None:
        assert CODE_NOT_VALID_TASK == "NOT_VALID_TASK"

    def test_code_not_exists_task(self) -> None:
        assert CODE_NOT_EXISTS_TASK == "NOT_EXISTS_TASK"

    def test_code_already_exists_task(self) -> None:
        assert CODE_ALREADY_EXISTS_TASK == "ALREADY_EXISTS_TASK"

    def test_code_not_found_task(self) -> None:
        assert CODE_NOT_FOUND_TASK == "NOT_FOUND_TASK"


class TestCodesTypes:
    def test_all_codes_are_strings(self) -> None:
        codes: list[str] = [
            CODE_ERROR_INTERNAL_LIBRARY,
            CODE_NOT_VALID_INTEGER,
            CODE_NOT_VALID_STATUS_TASK,
            CODE_NOT_VALID_PROPERTIES_TASK,
            CODE_NOT_VALID_TASK,
            CODE_NOT_EXISTS_TASK,
            CODE_ALREADY_EXISTS_TASK,
            CODE_NOT_FOUND_TASK,
        ]
        for code in codes:
            assert isinstance(code, str)
