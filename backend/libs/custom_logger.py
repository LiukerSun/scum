from loguru import logger


logger.add("logs/file_{time}.log", rotation="1 day")

logger = logger
