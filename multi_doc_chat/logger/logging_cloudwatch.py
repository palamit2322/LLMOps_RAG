import logging
import sys
from multi_doc_chat.config.config import settings

def setup_logging():
    logger = logging.getLogger(settings.PROJECT_NAME)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logging()

