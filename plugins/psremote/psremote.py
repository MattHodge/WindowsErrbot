from errbot import BotPlugin, botcmd, arg_botcmd
import subprocess # allow running of processes
import sys
import winrm
import json

class psremote(BotPlugin):
    @arg_botcmd('computername', type=str)
    @arg_botcmd('--port', dest='port', type=int, default=5985)
    def remotesvc(self, message, computername=None, port=None):
        """
        Gets services over WinRM
        """

        ps_script = """
            Get-Service
        """


        fullcomputername = computername + ":" + str(port)

        yield "Running command on {fullname}".format(
            fullname = fullcomputername
        )

        s = winrm.Session(fullcomputername, auth=('vagrant', 'vagrant'))
        r = s.run_ps(ps_script)

        yield "{stdout}".format(
            statuscode=r.status_code,
            stdout=r.std_out.decode('utf-8')
        )
