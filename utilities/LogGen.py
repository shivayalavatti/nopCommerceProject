import logging
class LogGen:
    @staticmethod
    def loggen():
        # Configure the logging
        logging.basicConfig(
            filename="./utilities/Logs/automation.log",
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )

        # Get the logger
        logger = logging.getLogger()

        # Set the logging level to INFO
        logger.setLevel(logging.INFO)

        # Return the logger
        return logger
