import logging
import sys
from stack_formatter import formatter
from stack_handler_filter import stderr_filter, stdout_filter

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.addFilter(stdout_filter)
stdout_handler.setFormatter(formatter)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.addFilter(stderr_filter)
stderr_handler.setFormatter(formatter)
