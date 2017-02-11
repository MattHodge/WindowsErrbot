from errbot import BotPlugin, botcmd

class hello(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def hello(self, msg, args):
        """Say hello to the world"""
        return "Hello, world!"

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
