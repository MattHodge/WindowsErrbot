from errbot import BotPlugin, botcmd, arg_botcmd

class demo(BotPlugin):
    """Example 'Hello, world!' plugin for Errbot"""

    @botcmd
    def demo2(self, msg, args):
        """Help for Demo 2"""

        demo2content = """
• Open VSCode
    • Look at the `plugins` directory
    • Look at `hello.py` - `hello` function
    • Explain the help header
• Run `!help hello` to show the contextual help
• Run `!hello`
• Run `!saymyname matt`
• Open VSCode
    • Look at `saymyname` function
"""
        yield demo2content
