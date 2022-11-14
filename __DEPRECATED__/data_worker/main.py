import time

import common.logging_setup as log_setup

logger = log_setup.setup_logger("data_worker")


while True:
    logger.debug("Working ...")
    time.sleep(1)