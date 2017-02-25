from errbot import BotPlugin, botcmd, arg_botcmd
import winrm

def run_remote_ps(computername, port, username, password, ps_script):
    """Function for running PowerShell via WinRM"""

    # join computername and port
    name_and_winrm_port = "{computername}:{port}".format(
        computername=computername,
        port=port
    )

    # Run the command remotley
    s = winrm.Session(name_and_winrm_port, auth=(username, password))
    r = s.run_ps(ps_script)

    # Create return object
    cmd_out = {
        'exit_code': r.status_code,
        'std_out': r.std_out.decode('cp1252')
    }
    
    return cmd_out

class psremote(BotPlugin):
    @arg_botcmd('computername', type=str)
    @arg_botcmd('--port', dest='port', type=int, default=5985)
    def restartpc(self, message, computername=None, port=None):
        """
        Restart Computer over WinRM
        """

        ps_script = """
            # sleep for demo purposes
            Start-Sleep -Seconds 5

            Restart-Computer -Force -Verbose
        """

        cmd_output = run_remote_ps(computername, port, 'vagrant', 'vagrant', ps_script)

        if cmd_output['exit_code'] == 0:
            yield ":white_check_mark: Computer \`{computername}\` has been restarted.".format(
                computername=computername
            )
        else:
            yield ":x: Unable to restart Computer \`{computername}\`".format(
                computername=computername
            )
