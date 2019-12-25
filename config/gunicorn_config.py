"""
Gunicorn Configuration

=====================
gunicorn configuration parameters
"""

import logging
import os

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("", "logging.json")
LOGGER = logging.getLogger(__name__)

# Log to stdout
accesslog = "-"

# The access log format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Log to stderr
errorlog = "-"

# Pre-load the application before the workers start. Needed to ensure app initialization/table creation
# happens only once
preload_app = True

# Number of gunicorn workers
# workers = cpu_count() * 2 + 1
workers = 1

# Set the worker class to gthread
worker_class = "gevent"

# Set the number of threads
# threads = cpu_count() * 2
threads = 1

# Set the timeout for requests (purposefully set to a very high value of 1 hour)
timeout = 3600

# Set the python path
pythonpath = "/usr/local/lib/python3"
