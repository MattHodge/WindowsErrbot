from errbot import BotPlugin, botcmd, arg_botcmd

class hello(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        yield "Hello, world!"

    @botcmd
    def hellopretty(self, msg, args):
        """Say hello to the world, but more pretty this time"""
        yield "You want more pretty?"
        yield "How about some \*bold\* then?"
        yield "\> Or maybe a block quote is more to your liking?"
        yield "What if you want to `emphasize` something?"
        # Similar to PowerShell Here-String
        code_block = """
Or if you have a code block:
\`\`\`
Write-Output "Welcome to PSConf2017!"
Write-Output "In Germany!"
\`\`\`
"""
        yield code_block
        yield "https://api.giphy.com/img/giphy_translate.gif"

    @arg_botcmd('name', type=str)
    def saymyname(self, message, name=None):
        """Say the entered name"""
        yield "Hello, {first_name}".format(
            first_name=name
        )

    @arg_botcmd('name', type=str)
    @arg_botcmd('--last-name', dest='last_name', type=str)
    def saymynameagain(self, message, name=None, last_name=None):
        """Say the name and optional last name"""
        if last_name:
            yield "Hello again, {first_name} {last_name}".format(
                first_name=name,
                last_name=last_name,
            )
        else:
            yield "Hello again, {first_name}".format(
                first_name=name
            )
