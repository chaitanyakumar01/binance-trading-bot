import logging

def setup_logger():
    """
    Configures logging to output to both the terminal and the 'bot.log' file.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Prevent double printing if handlers already exist
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler to save logs
    file_handler = logging.FileHandler('bot.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console handler to print logs in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger