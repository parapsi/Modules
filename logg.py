import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("file_log.log", mode="w")
formatter = logging.Formatter("%(name)s - %(asctime)s - %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)