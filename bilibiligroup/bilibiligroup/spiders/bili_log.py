import logging

class Mylog:
    logging.basicConfig(
        level=logging.CRITICAL,
        filename='crawl.log',
        filemode='a',
        format='%(asctime)s %(filename)s %(levelname)s %(message)s'
    )
    def InfoLog(self, message):
        logging.info(message)
    def WaringLog(self, warn):
        logging.warning(warn)
    def ErrorLog(self, error):
        logging.error(error)
    def CriticalLog(self, message):
        logging.critical(message)
