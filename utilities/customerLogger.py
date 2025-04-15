import logging
class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename='..\\logs\\automation.log', format='%(asctime)s:%(levelname)s: %m/%d%y %I:%M')
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger