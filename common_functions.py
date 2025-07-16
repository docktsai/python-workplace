import logging

common_logger = logging.getLogger("data_extract.common_functions")

def com_function1() -> None:
    common_logger.debug(" --- to test common function 1 logging")

def com_function2() -> None:
    common_logger.debug(" --- to test common function 2 logging")
