from task_manager.constants.codes import CODE_ERROR_INTERNAL_LIBRARY
from task_manager.constants.messages import MESSAGE_ERROR_INTERNAL_LIBRARY


class BaseError(Exception):
    message: str = MESSAGE_ERROR_INTERNAL_LIBRARY
    code: str = CODE_ERROR_INTERNAL_LIBRARY

    def __init__(
        self,
        code: str = code,
        message: str | None = None,
    ):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        super().__init__(self.message)


class ValidationError(BaseError):
    message = "Validation error"


class AuthenticationError(BaseError):
    message = "Authentication error"


class NotFoundError(BaseError):
    message = "Resource not found"


class ConflictError(BaseError):
    message = "Conflict error"


class BusinessError(BaseError):
    message = "Business rule violated"


class InternalError(BaseError):
    message = "Internal error"
