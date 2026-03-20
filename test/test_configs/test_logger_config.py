import logging

from task_manager.configs.logger_config import setup_logger


class TestSetupLoggerReturn:
    def test_returns_logger_instance(self) -> None:
        logger = setup_logger("test.return")
        assert isinstance(logger, logging.Logger)

    def test_logger_name_matches(self) -> None:
        logger = setup_logger("test.name")
        assert logger.name == "test.name"

    def test_default_name(self) -> None:
        logger = setup_logger()
        assert logger.name == "template-library-python"


class TestSetupLoggerLevel:
    def test_logger_level_is_debug(self) -> None:
        logger = setup_logger("test.level")
        assert logger.level == logging.DEBUG


class TestSetupLoggerHandlers:
    def test_logger_has_handler(self) -> None:
        logger = setup_logger("test.handlers")
        assert len(logger.handlers) >= 1

    def test_handler_is_stream_handler(self) -> None:
        logger = setup_logger("test.stream")
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)

    def test_no_duplicate_handlers_on_repeated_calls(self) -> None:
        name = "test.no_duplicates"
        logger_first = setup_logger(name)
        handler_count = len(logger_first.handlers)
        logger_second = setup_logger(name)
        assert len(logger_second.handlers) == handler_count


class TestSetupLoggerFormatter:
    def test_handler_has_formatter(self) -> None:
        logger = setup_logger("test.formatter")
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        assert stream_handlers[0].formatter is not None

    def test_formatter_includes_levelname(self) -> None:
        logger = setup_logger("test.formatter.levelname")
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        fmt = stream_handlers[0].formatter._fmt
        assert "%(levelname)s" in fmt

    def test_formatter_includes_message(self) -> None:
        logger = setup_logger("test.formatter.message")
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        fmt = stream_handlers[0].formatter._fmt
        assert "%(message)s" in fmt

    def test_formatter_includes_asctime(self) -> None:
        logger = setup_logger("test.formatter.asctime")
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        fmt = stream_handlers[0].formatter._fmt
        assert "%(asctime)s" in fmt

    def test_formatter_includes_name(self) -> None:
        logger = setup_logger("test.formatter.name")
        stream_handlers = [h for h in logger.handlers if isinstance(h, logging.StreamHandler)]
        fmt = stream_handlers[0].formatter._fmt
        assert "%(name)s" in fmt
