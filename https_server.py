import log as log
import bot
import constants as const
from flask import Flask, request, Response
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberFailedRequest, ViberUnsubscribedRequest, ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest

light_on_bot = bot.Bot()
light_on_bot_api = light_on_bot.create_bot()
app = Flask(__name__)


@app.route('/', methods=['POST'])
def incoming():
    log.logger.debug("Received request. post data: {0}".format(request.get_data()))

    viber_request = light_on_bot_api.parse_request(request.get_data().decode('utf8'))

    if isinstance(viber_request, ViberMessageRequest):
        log.logger.debug(viber_request.message)
        light_on_bot_api.send_messages(viber_request.sender.id,
                                       [TextMessage(None, None, light_on_bot.answer_light_on(), None)])

    elif isinstance(viber_request, ViberConversationStartedRequest) or isinstance(viber_request, ViberSubscribedRequest):
        light_on_bot_api.send_messages(viber_request.sender.id, [TextMessage(None, None, const.MSG_WELCOME, None)])
    elif isinstance(viber_request, ViberUnsubscribedRequest):
        light_on_bot_api.send_messages(viber_request.sender.id, [TextMessage(None, None, const.MSG_BYE, None)])
    elif isinstance(viber_request, ViberFailedRequest):
        log.logger.warn("Client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)
