from errbot import BotPlugin, botcmd, arg_botcmd
import subprocess # allow running of processes
import sys
import winrm
import json

class psexample(BotPlugin):
    """Example of getting processes using PowerShell"""

    @botcmd
    def getdate(self, msg, args):
        """Get the date from PowerShell"""

        p = subprocess.check_output(['powershell.exe', '-command', '& { Get-Date }'])
        decoded_output = p.decode('cp1252')
        return "The date is: " + decoded_output

    @arg_botcmd('process_name', type=str)
    def getproc(self, msg, process_name=None):
        """Get a PowerShell Process"""

        get_proc_cmd = "& { Get-Process -Name %s }" % process_name

        p = subprocess.check_output(['powershell.exe', '-command', get_proc_cmd])
        decoded_output = p.decode('cp1252')
        return decoded_output

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

    @arg_botcmd('service_name', type=str)
    def getservice(self, msg, service_name=None):
        """Get Information on PowerShell Service"""

        # Return the service object as json
        get_svc_cmd = "& { Get-Service -Name %s | ConvertTo-Json -Compress }" % service_name

        p = subprocess.check_output(['powershell.exe', '-command', get_svc_cmd])

        # convert the json to an object
        json_output = json.loads(p.decode('cp1252'))

        return json_output['DisplayName']
