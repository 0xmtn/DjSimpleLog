import logging
# Setting up the logger
logging.basicConfig(level=logging.DEBUG, filename="/dev/null")
# Getting all the user added apps
apps = [ app for app in INSTALLED_APPS if "django" not in app ]
# Creating file path list with log files appended to app names in apps list
apps_log_files = [ app + "/logs/access.log" for app in apps ]
# Create logging handlers
log_handlers = [ logging.FileHandler(i) for i in apps_log_files ]
# Lambda to set levels of log handlers
set_level = lambda a: a.setLevel(logging.DEBUG)
# Map the lamdba to the log_handlers list
map(set_level, log_handlers)
# Set up the format of logs
formatter = logging.Formatter('[%(asctime)-12s] %(message)-8s')
# Lambda to set formatter to log handlers
set_formatter = lambda a: a.setFormatter(formatter)
# Map the lambda to the log handlers list
map(set_formatter, log_handlers)
#creating loggers and adding log_handlers to them
for app, lhf in zip(apps, log_handlers):
    logging.getLogger(app).addHandler(lhf)
