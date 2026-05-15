"""
Logging configuration for Personal Weight Tracker.
Provides centralized logging setup for the application.
"""
import logging
import os
from datetime import datetime
from pathlib import Path


def setup_logger(
    name: str = "weight_tracker",
    log_level: str = "INFO",
    log_file: str = None,
    console_output: bool = True
) -> logging.Logger:
    """
    Set up and configure a logger for the application.
    
    Args:
        name: Logger name (default: "weight_tracker")
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file (optional, creates if doesn't exist)
        console_output: Whether to output logs to console (default: True)
        
    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    simple_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # Console handler
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        logger.addHandler(console_handler)
    
    # File handler
    if log_file:
        # Create logs directory if it doesn't exist
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        logger.addHandler(file_handler)
    
    return logger


def get_logger(name: str = "weight_tracker") -> logging.Logger:
    """
    Get an existing logger or create a new one with default settings.
    
    Args:
        name: Logger name
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    
    # If logger doesn't have handlers, set it up with defaults
    if not logger.handlers:
        log_level = os.getenv("LOG_LEVEL", "INFO")
        log_file = os.getenv("LOG_FILE", "logs/app.log")
        return setup_logger(name, log_level, log_file)
    
    return logger


# Create a default logger instance
default_logger = get_logger()


def log_function_call(func):
    """
    Decorator to log function calls with arguments and return values.
    
    Usage:
        @log_function_call
        def my_function(arg1, arg2):
            return result
    """
    def wrapper(*args, **kwargs):
        logger = get_logger()
        func_name = func.__name__
        logger.debug(f"Calling {func_name} with args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logger.debug(f"{func_name} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func_name}: {str(e)}", exc_info=True)
            raise
    
    return wrapper


def log_error(error: Exception, context: str = "") -> None:
    """
    Log an error with context information.
    
    Args:
        error: The exception that occurred
        context: Additional context about where/why the error occurred
    """
    logger = get_logger()
    if context:
        logger.error(f"{context}: {str(error)}", exc_info=True)
    else:
        logger.error(f"Error occurred: {str(error)}", exc_info=True)


def log_info(message: str) -> None:
    """
    Log an informational message.
    
    Args:
        message: The message to log
    """
    logger = get_logger()
    logger.info(message)


def log_warning(message: str) -> None:
    """
    Log a warning message.
    
    Args:
        message: The warning message to log
    """
    logger = get_logger()
    logger.warning(message)


def log_debug(message: str) -> None:
    """
    Log a debug message.
    
    Args:
        message: The debug message to log
    """
    logger = get_logger()
    logger.debug(message)

# Made with Bob
