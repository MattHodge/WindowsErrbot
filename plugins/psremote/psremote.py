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

    @arg_botcmd('computername', type=str)
    @arg_botcmd('feature_name', type=str)
    @arg_botcmd('--port', dest='port', type=int, default=5985)
    @arg_botcmd('--ensure', dest='ensure', type=str, default='Present')
    def dscfeature(self, message, computername=None, port=None, ensure=None, feature_name=None):
        """
        Install DSC Features Remotley
        """

        ps_script = """
            $VerbosePreference="Continue"

            $splat = @{{
                Name = 'WindowsFeature'
                Method = 'Set'
                Property = @{{
                    Name = '{feature_name}'
                    Ensure = '{ensure}'
                }}
                ModuleName = 'PSDesiredStateConfiguration'
                Verbose = $true
            }}

            # Capture verbose output
            $dscout = Invoke-DscResource @splat 4>&1

            # Set output to file so it comes back out as stdout
            Set-Content -Path $env:TEMP\dscout.txt -Value $dscout
            Get-Content -Path $env:TEMP\dscout.txt
        """.format(
            feature_name=feature_name,
            ensure=ensure
        )

        cmd_output = run_remote_ps(computername, port, 'vagrant', 'vagrant', ps_script)

        yield "\`\`\`{stdout}\`\`\`".format(
            stdout=cmd_output['std_out']
        )

        if cmd_output['exit_code'] == 0:
            yield ":white_check_mark: \`{feature_name}\` has been set to *{ensure}* on \`{computername}\`.".format(
                feature_name=feature_name,
                ensure=ensure,
                computername=computername
            )
        else:
            yield ":x: Unable to set \`{feature_name}\` as *ensure* on Computer \`{computername}\`".format(
                feature_name=feature_name,
                ensure=ensure,
                computername=computername
            )
