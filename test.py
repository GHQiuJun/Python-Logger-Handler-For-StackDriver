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

'''
output：
{"timestamp": "2018-12-25T07:23:31.888437Z", "severity": 40, "message": "this is a error message"}
{"timestamp": "2018-12-25T07:23:31.887942Z", "severity": 20, "message": "this a info message"}
'''

# or add handler to root logger
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(stderr_handler)
root.addHandler(stdout_handler)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# default，app.logger will send log to stderr
app.run(host='0.0.0.0', port=4001)
'''
output：
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
{"timestamp": "2018-12-25T07:26:59.281661Z", "severity": 20, "message": " * Running on http://0.0.0.0:4001/ (Press CTRL+C to quit)"}
{"timestamp": "2018-12-25T07:27:04.344244Z", "severity": 20, "message": "127.0.0.1 - - [25/Dec/2018 15:27:04] \"GET / HTTP/1.1\" 200 -"}
'''
