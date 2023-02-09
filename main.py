import log as log
import https_server as hs
import constants as const

if __name__ == '__main__':
    log.logger.info('Starting the app.')
    hs.app.run(host=const.HOST, port=const.PORT, debug=True)
