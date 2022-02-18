'''
normally I run "logger" from my own private function library, but since this is a public project, I shouldn't do that.
'''

import colorlog
import logging
#======================================================================
# logger
#======================================================================
def logger(log_filepath,logger_name,debug=None):
    """Log plain text to file and to terminal with colors
    
    https://awesomeopensource.com/project/borntyping/python-colorlog?

    use debug=True to turn on debug logging.
    """

    logger = logging.getLogger(logger_name)

    # Log to file (but not to terminal)
    logfile_handler = logging.FileHandler(log_filepath, encoding='utf-8')
    plain_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    logfile_handler.setFormatter(plain_formatter)
    if debug:
        logfile_handler.setLevel(logging.DEBUG) # oh... Does that mean we log all debugs in the logs? hm.
    else:
        logfile_handler.setLevel(logging.INFO) # Let's try this instead. Time to reduce the writes a bit.
    # honestly, I don't think this does anything? I'm not sure...

    # https://docs.python.org/3/library/logging.html look for "LogRecord attributes"
    # https://realpython.com/python-string-formatting/
    # Logging info level to stdout with colors
    terminal_handler = colorlog.StreamHandler()
    color_formatter = colorlog.ColoredFormatter(
        #"%(log_color)s%(levelname)-8s%(reset)s %(asctime)s %(cyan)s%(message)s",
        "%(log_color)s%(asctime)-2s%(reset)s%(cyan)s %(message)s", # theoretically that'll make the date COLOR show if it's an error or info.
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'blue',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    if debug:
        logger.setLevel(my_logger.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    terminal_handler.setFormatter(color_formatter)

    # Add handlers to logger
    logger.addHandler(logfile_handler)
    logger.addHandler(terminal_handler)
    return logger


# logs isn't auto created, so that can throw an error. Just make the directory if that happens.
# you can automate creating that folder, but I've had issues where I accidentally started the scripts in the wrong folder
# and then it starts making "logs" folders everywhere. Better if it throws an error in my opinion.
my_logger = logger(log_filepath='logs/helper_functions.log', logger_name='helper_functions')