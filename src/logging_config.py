from loguru import logger
import sys
from .config import settings

def configure_logging() -> None:
    logger.remove()
    level = settings.log_level.upper()
    # structured format with time and level
    logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | {module}:{function}:{line} - {message}", level=level)
    # Example: send to file rotating (optional in prod)
    logger.add("logs/goldeye.log", rotation="10 MB", retention="7 days", level=level)

configure_logging()
