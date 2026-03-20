import pytest

from task_manager.constants.codes import CODE_ERROR_INTERNAL_LIBRARY
from task_manager.constants.messages import MESSAGE_ERROR_INTERNAL_LIBRARY
from task_manager.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    def test_is_exception_subclass(self) -> None:
        assert issubclass(BaseError, Exception)

    def test_default_code(self) -> None:
        error = BaseError()
        assert error.code == CODE_ERROR_INTERNAL_LIBRARY

    def test_default_message(self) -> None:
        error = BaseError()
        assert error.message == MESSAGE_ERROR_INTERNAL_LIBRARY

    def test_custom_code(self) -> None:
        error = BaseError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    def test_custom_message(self) -> None:
        error = BaseError(message="Custom message")
        assert error.message == "Custom message"

    def test_custom_code_and_message(self) -> None:
        error = BaseError(code="MY_CODE", message="My message")
        assert error.code == "MY_CODE"
        assert error.message == "My message"

    def test_can_be_raised(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()

    def test_message_propagated_to_exception_args(self) -> None:
        error = BaseError(message="Propagated message")
        assert "Propagated message" in str(error)


class TestValidationError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(ValidationError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(ValidationError):
            raise ValidationError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ValidationError()

    def test_caught_as_exception(self) -> None:
        with pytest.raises(Exception):
            raise ValidationError()

    def test_custom_code_and_message(self) -> None:
        error = ValidationError(code="VAL_CODE", message="Val message")
        assert error.code == "VAL_CODE"
        assert error.message == "Val message"


class TestAuthenticationError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(AuthenticationError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(AuthenticationError):
            raise AuthenticationError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise AuthenticationError()

    def test_custom_code_and_message(self) -> None:
        error = AuthenticationError(code="AUTH_CODE", message="Auth message")
        assert error.code == "AUTH_CODE"
        assert error.message == "Auth message"


class TestNotFoundError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(NotFoundError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(NotFoundError):
            raise NotFoundError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise NotFoundError()

    def test_custom_code_and_message(self) -> None:
        error = NotFoundError(code="NF_CODE", message="Not found message")
        assert error.code == "NF_CODE"
        assert error.message == "Not found message"


class TestConflictError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(ConflictError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(ConflictError):
            raise ConflictError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ConflictError()

    def test_custom_code_and_message(self) -> None:
        error = ConflictError(code="CONF_CODE", message="Conflict message")
        assert error.code == "CONF_CODE"
        assert error.message == "Conflict message"


class TestBusinessError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(BusinessError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(BusinessError):
            raise BusinessError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise BusinessError()

    def test_custom_code_and_message(self) -> None:
        error = BusinessError(code="BIZ_CODE", message="Business message")
        assert error.code == "BIZ_CODE"
        assert error.message == "Business message"


class TestInternalError:
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(InternalError, BaseError)

    def test_can_be_raised(self) -> None:
        with pytest.raises(InternalError):
            raise InternalError()

    def test_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise InternalError()

    def test_custom_code_and_message(self) -> None:
        error = InternalError(code="INT_CODE", message="Internal message")
        assert error.code == "INT_CODE"
        assert error.message == "Internal message"
