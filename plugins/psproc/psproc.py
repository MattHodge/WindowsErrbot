from errbot import BotPlugin, botcmd
import subprocess # allow running of processes
import sys
import winrm

class psproc(BotPlugin):
    """Example of getting processes using PowerShell"""

    @botcmd
    def getdate(self, msg, args):
        """Get the date from PowerShell"""

        p = subprocess.check_output(['powershell.exe', '-command', '& { Get-Date }'])
        decoded_output = p.decode('cp1252')
        return "The date is: " + decoded_output

    @botcmd
    def getmem(self, msg, args):
        """Get the the system memory from PowerShell"""

        ps_script = """
        & {
            $mem = Get-CimInstance -class "cim_physicalmemory" | Select-Object Capacity
            Write-Output "Installed Memory: ``$($mem.Capacity / 1MB)`` mb"
        }
        """

        p = subprocess.check_output(['powershell.exe', '-command', ps_script])
        decoded_output = p.decode('cp1252')
        return decoded_output
