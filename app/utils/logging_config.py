import logging
from pathlib import Path

from app.config.settings import settings


def configure_logging() -> None:
    """Configure application logging."""

    settings.log_directory.mkdir(parents=True, exist_ok=True)

    log_file = settings.log_directory / "application.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )