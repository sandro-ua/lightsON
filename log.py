import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('logfile.log', 'w', 'utf-8')
formatter = logging.Formatter("%(asctime)s %(name)-20s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_user_action(msg, name, user_id, country):
    logger.info("{0} | sender_name: [{1}] sender_id: [{2}] sender_country: [{3}]".format(msg, name, user_id, country))
