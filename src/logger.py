import logging


def setup_logger(name: str, log_file: str) -> logging.getLogger():
    """Логгер для модулей, которвый записывает лог в файл"""
    logger = logging.getLogger(name)
    handler = logging.FileHandler(log_file, "w")
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
