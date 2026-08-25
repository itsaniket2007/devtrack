from services.devTrack import DevTrack
from utils.logger import logger


logger.info("DevTrack application started")

app = DevTrack()
app.menu()