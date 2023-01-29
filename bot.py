import datetime as dt

import constants as const
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
import log as log
import dns.resolver as resolver


class Bot:

    def __init__(self):
        self.bot_config = BotConfiguration(
            name=const.VIBER_BOT_NAME,
            auth_token=const.VIBER_AUTH_TOKEN,
            avatar=const.VIBER_AVATAR_PIC_PATH
        )

    def create_bot(self):
        return Api(self.bot_config)

    def answer_light_on(self):
        if self.check_if_online(const.DDNS_VALUE):
            return const.MSG_LIGHT_ON + dt.datetime.now().strftime(const.TIME_FORMAT)
        else:
            return const.MSG_LIGHT_OFF + dt.datetime.now().strftime(const.TIME_FORMAT)

    @staticmethod
    def check_if_online(url):
        try:
            result = resolver.resolve(url)
            log.logger.debug("Server IP is: {}".format(result.nameserver))
            return True
        except (resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers) as e:
            log.logger.warn(f"{url}: is Not reachable \nErr: {e}")
            return False

