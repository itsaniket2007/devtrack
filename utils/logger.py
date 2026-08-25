import logging


logging.basicConfig(
    filename="logs/devtrack.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger("DevTrack")