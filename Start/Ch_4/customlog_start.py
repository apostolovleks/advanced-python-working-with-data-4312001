# Demonstrate how to customize logging output

import logging


# TODO: add another function to log from
def func():
    logging.debug("This is a debug-level message", extra=extdata)


# set the output file and debug level, and
# TODO: use a custom formatting specification
fmstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
datestr = "%d/%m/%Y %H:%M:%S %p"
extdata = {"user": "John Doe"}
logging.basicConfig(
    filename="/workspaces/advanced-python-working-with-data-4312001/Start/Ch_4/output.log",
    level=logging.DEBUG,
    format=fmstr,
    datefmt=datestr,
)

logging.info("This is an info-level log message", extra=extdata)
logging.warning("This is a warning-level message", extra=extdata)
func()
