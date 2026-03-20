from task_manager.constants.messages import (
    MESSAGE_ALREADY_EXISTS_TASK,
    MESSAGE_ERROR_INTERNAL_LIBRARY,
    MESSAGE_NOT_EXISTS_TASK,
    MESSAGE_NOT_FOUND_TASK,
    MESSAGE_NOT_VALID_INTEGER,
    MESSAGE_NOT_VALID_PROPERTIES_TASK,
    MESSAGE_NOT_VALID_STATUS_TASK,
    MESSAGE_NOT_VALID_TASK,
)


class TestMessagesValues:
    def test_message_error_internal_library(self) -> None:
        assert MESSAGE_ERROR_INTERNAL_LIBRARY == "Internal library error."

    def test_message_not_valid_integer(self) -> None:
        assert MESSAGE_NOT_VALID_INTEGER == "The value entered is not a valid integer."

    def test_message_not_valid_status_task(self) -> None:
        assert MESSAGE_NOT_VALID_STATUS_TASK == "The status entered is not a valid."

    def test_message_not_valid_properties_task(self) -> None:
        assert MESSAGE_NOT_VALID_PROPERTIES_TASK == "The properties entered are not valid."

    def test_message_not_valid_task(self) -> None:
        assert MESSAGE_NOT_VALID_TASK == "The task entered is not valid."

    def test_message_not_exists_task(self) -> None:
        assert MESSAGE_NOT_EXISTS_TASK == "The task not exists."

    def test_message_already_exists_task(self) -> None:
        assert MESSAGE_ALREADY_EXISTS_TASK == "The task already exists."

    def test_message_not_found_task(self) -> None:
        assert MESSAGE_NOT_FOUND_TASK == "Not found task."


class TestMessagesTypes:
    def test_all_messages_are_strings(self) -> None:
        messages: list[str] = [
            MESSAGE_ERROR_INTERNAL_LIBRARY,
            MESSAGE_NOT_VALID_INTEGER,
            MESSAGE_NOT_VALID_STATUS_TASK,
            MESSAGE_NOT_VALID_PROPERTIES_TASK,
            MESSAGE_NOT_VALID_TASK,
            MESSAGE_NOT_EXISTS_TASK,
            MESSAGE_ALREADY_EXISTS_TASK,
            MESSAGE_NOT_FOUND_TASK,
        ]
        for message in messages:
            assert isinstance(message, str)
