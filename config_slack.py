import logging
import os

BACKEND = 'Slack'
BOT_DATA_DIR = 'C:\\errdata'
BOT_EXTRA_PLUGIN_DIR = 'C:\\vagrant\\plugins'
AUTOINSTALL_DEPS = True
BOT_LOG_FILE = 'C:\\errdata\\err.log'
BOT_LOG_LEVEL = logging.DEBUG
BOT_ASYNC = True
BOT_IDENTITY = {
    'token': os.environ['slack_api_key'],
}
BOT_ADMINS = ('gbin@localhost',)
CHATROOM_FN = 'errbot'
BOT_PREFIX = '!'
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
