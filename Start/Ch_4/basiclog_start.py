# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging


# TODO: Use basicConfig to configure logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="/workspaces/advanced-python-working-with-data-4312001/Start/Ch_4/output.log",
    filemode="w",
)

# TODO: Try out each of the log levels
logging.debug("Debug message")
logging.info("Info message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")

# TODO: Output formatted strings to the log
x = "string"
y = 10
logging.info(f"Here is a {x} variavble and int: {y}")
