import logging

BOT_DATA_DIR = 'C:\\errdata'
BOT_EXTRA_PLUGIN_DIR = 'C:\\vagrant\\plugins'
AUTOINSTALL_DEPS = True
BOT_LOG_FILE = 'C:\\errdata\\err.log'
BOT_LOG_LEVEL = logging.DEBUG
BOT_ASYNC = True
BOT_IDENTITY = {
    # XMPP (Jabber) mode
    'username': 'err@localhost',  # The JID of the user you have created for the bot
    'password': 'changeme',       # The corresponding password for this user
}
BOT_ADMINS = ('gbin@localhost',)
CHATROOM_FN = 'errbot'
BOT_PREFIX = '!'
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
