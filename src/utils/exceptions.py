class InvalidTaskStateError(Exception):
    """Exception raised when an invalid state is set for a Task."""
    pass

class InvalidTaskEdit(Exception):
    """Exception raised when try to edit a task without any params."""
    pass

class InvalidStateOrIdError(Exception):
    """Exception raised when an invalid state or id is set for a Task."""
    pass

class InvalidTaskIdError(Exception):
    """Exception raised when an invalid id is set for a Task."""
    pass

class InvalidTaskError(Exception):
    """Exception raised when an invalid Task is setted."""
    pass

class TaskAlreadyExistsError(Exception):
    """Exception raised when an Task already exists."""
    pass

class TaskNotFoundError(Exception):
    """Exception raised when a task is not found in the TaskManager."""
    pass