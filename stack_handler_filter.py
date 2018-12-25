import logging


# handler filter
def stderr_filter(record):
    if record.levelno >= logging.WARNING:
        return True
    return False


def stdout_filter(record):
    if logging.WARNING > record.levelno >= logging.DEBUG:
        return True
    return False
