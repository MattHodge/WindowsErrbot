import logging
import os

AUTOINSTALL_DEPS = True
BACKEND = 'Slack'
BOT_ADMINS = ('@hodge',)
BOT_ALT_PREFIXES = ('@calculon',)
BOT_ALT_PREFIX_SEPARATORS = (':', ',', ';')
BOT_ALT_PREFIX_CASEINSENSITIVE = True
BOT_DATA_DIR = './data'
BOT_EXTRA_PLUGIN_DIR = './plugins'
BOT_IDENTITY = { 'token': os.environ['slack_api_key'] }
BOT_LOG_FILE = './data/err.log'
BOT_LOG_LEVEL = logging.DEBUG
BOT_PREFIX = '!'
CHATROOM_PRESENCE = ()
DIVERT_TO_PRIVATE = ('help')
