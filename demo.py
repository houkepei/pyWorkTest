import logging

logger = logging.getLogger("loggingmodule.NomalLogger")
handler = logging.FileHandler("one.log")
formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# test
logger.debug("this is a debug msg!")
logger.info("this is a info msg!")