from pythonjsonlogger import jsonlogger
from datetime import datetime


class StackJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(StackJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # utc
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']


# add fields you want to use, add severity field for stack_driver
formatter = StackJsonFormatter('(timestamp) (severity) (levelname) (message)')
