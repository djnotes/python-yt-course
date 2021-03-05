

import logging

#Setting logging configuration
logging.basicConfig(filename = "log.txt")
logging.log(logging.ERROR, "This is a message")


#Recommended way of logging 
logger = logging.getLogger(__name__)
logger.log(logging.ERROR, "This is a message")
logger.log(logging.WARN, "This is a warning")
logger.log(logging.DEBUG, "This is a debug message")

elogger = logging.getLogger(f"{__name__}.error")
elogger.addHandler(logging.FileHandler("errors.log"))
elogger.setLevel(logging.ERROR)

ilogger = logging.getLogger(__name__ + ".info")
ilogger.addHandler(logging.FileHandler("infomation.log"))
ilogger.setLevel(logging.INFO)

wlogger = logging.getLogger(__name__ + ".warn")
wlogger.addHandler(logging.FileHandler("warning.log"))
wlogger.setLevel(logging.WARNING)

#Testing our loggers
elogger.error("This is an error sent to custom logger")
ilogger.info("This is an info log sent to custom logger")
wlogger.warning("This is a warning sent to custom logger")









