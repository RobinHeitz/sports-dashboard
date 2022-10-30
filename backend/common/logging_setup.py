import logging
import pathlib

loggers = list()

def setup_logger(name:str, level: int = logging.DEBUG, stream_handler = True, file_handler = True) -> logging.Logger:
    """Setups logger with stream-handler and file-handler, returns logging.Logger-Instance.
    """

    logger = logging.getLogger(name)

    global loggers
    loggers.append(name)

    logger.setLevel(level)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    if stream_handler is True:
        sh = logging.StreamHandler()
        sh.setLevel(level)
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    
    if file_handler is True:
        file_name = f"{name.lower()}.log"
        log_dir = pathlib.Path("logs")

        if not log_dir.exists():
            pathlib.Path.mkdir(log_dir)
        
        path = log_dir / file_name

        fh = logging.FileHandler(str(path))
        fh.setLevel(level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    return logger