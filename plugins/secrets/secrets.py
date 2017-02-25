from errbot import BotPlugin, botcmd, arg_botcmd
import keyring

class secrets(BotPlugin):
    @botcmd
    def getkey(self, msg, args):
        """
        Get a password from the Windows Password Vault
        """

        test_password = keyring.get_password('demo','username')

        if not test_password:
            yield "No password has been set for username"
        else:
            yield "The password is **{}**".format(
                test_password
            )

