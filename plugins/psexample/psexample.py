from errbot import BotPlugin, botcmd, arg_botcmd
import subprocess  # allow running of processes
import sys


def run_ps_inline(ps_script):
    """Function for running PowerShell locally"""
    # Prepare the script to pass to PowerShell Command Line
    script_block = "& { %s }" % ps_script

    # Execute a subprocess
    p = subprocess.check_output(['powershell.exe', '-command', script_block])

    # Decode the output
    output = p.decode('cp1252')

    # return the output
    return output


def run_ps_function_file(file, function_name, params):
    """Function for dot sourcing a PowerShell script and passing it paramaters"""

    # Build a full path to the PowerShell script
    full_file_path = sys.path[0] + '\\plugins\\psexample\\' + file

    # Prepare the script to pass to PowerShell Command Line
    script_block = "& { . %s ; %s %s }" % (full_file_path, function_name, params)

    # Execute a subprocess
    p = subprocess.check_output(['powershell.exe', '-command', script_block])

    # Decode the output
    output = p.decode('cp1252')

    # return the output
    return output


class psexample(BotPlugin):
    """Example of getting processes using PowerShell"""
    # Basic PowerShell Example
    @botcmd
    def getdate(self, msg, args):
        """Get the date from PowerShell"""

        # Build the PowerShell Script
        ps_script = "Get-Date"

        # Run PowerShell Locally
        ps_result = run_ps_inline(ps_script)

        # Build a string with the result and return it
        yield "The date is: {date}".format(
            date=ps_result
        )

    # Formating for Slack inside the PowerShell Script
    @botcmd
    def getlastboot(self, msg, args):
        """Get the last boot time of the system"""

        # Build the PowerShell Script
        ps_script = """
            $lastboot = Get-CimInstance -ClassName win32_operatingsystem | Select-Object lastbootuptime
            Write-Output "This system last booted up on: ``$($lastboot.lastbootuptime)``"
        """

        # Run PowerShell Locally
        ps_result = run_ps_inline(ps_script)

        yield ps_result

    @arg_botcmd('svc_name', type=str)
    def getsvc(self, msg, svc_name=None):
        """Get a PowerShell Service Status"""

        ps_params = "-Name %s" % svc_name
        ps_result = run_ps_function_file('Get-ServiceBot.ps1', 'Get-ServiceBot', ps_params)
        yield ps_result

        # # Enable logging to event viewer
        # ps_script = "Write-EventLog -LogName Application -Source 'Errbot' -EntryType Information -EventID 1 -Message 'User {user} ran this command: {command}. The result was {result}'".format(
        #     user=msg.frm,
        #     command=msg,
        #     result=ps_result
        # )
        # run_ps_inline(ps_script)

