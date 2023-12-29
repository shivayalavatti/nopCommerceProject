import logging
import os

if not os.path.exists("Logs"):
    os.makedirs("Logs")
    print("Current Working Directory:", os.getcwd())


class LogGen:
    @staticmethod
    def loggen():

        logging.basicConfig(filename="./Logs/automation2.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger