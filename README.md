## Python Logger Handler For StackDriver

- use logger handler properly send log to stderr、stdout

### how to use logger in gcp

- 1、[Configure a standard logging package to send the logs you write to Stackdriver Logging](https://cloud.google.com/logging/docs/setup/)
- 2、[use Logging Agent collect log ,send to Stackdriver](https://cloud.google.com/logging/docs/agent/)


### there is maybe a problem when you use Logging Agent collect log ?

- 1、Don't properly send log to stderr、stdout, all log in StackDriver is error
- 2、warn will be regard as error if there is no severity field


## Usage
```markdown
// a new logger 

from stack_handler import stdout_handler, stderr_handler
import logging
from flask import Flask

# init a logger
stack_logger = logging.getLogger('stack_logger')
stack_logger.setLevel(logging.DEBUG)

# add stdout_handler、stderr_handler to logger
stack_logger.addHandler(stderr_handler)
stack_logger.addHandler(stdout_handler)

stack_logger.info('this a info message')
stack_logger.error('this is a error message')

output：
{"timestamp": "2018-12-25T07:23:31.888437Z", "severity": 40, "message": "this is a error message"}
{"timestamp": "2018-12-25T07:23:31.887942Z", "severity": 20, "message": "this a info message"}


// add to root logger
from stack_handler import stdout_handler, stderr_handler
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(stderr_handler)
root.addHandler(stdout_handler)

root.error('this is error')
root.info('this is info')

output:
{"timestamp": "2018-12-25T08:08:06.174206Z", "severity": "INFO", "message": "this is info"}
{"timestamp": "2018-12-25T08:08:06.173621Z", "severity": "ERROR", "message": "this is error"}
```