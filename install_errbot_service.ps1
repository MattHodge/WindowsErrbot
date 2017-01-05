$errbotExePath = (Get-Command errbot).Source
$errbotPath = 'C:\vagrant'

# Install nssm
if (!(Get-Command -Name 'nssm' -ErrorAction SilentlyContinue))
{
    choco install nssm -y
}
else
{
    Write-Output "nssm is already installed"
}

& nssm install errbot $errbotExePath -c config_slack.py
& nssm set errbot AppDirectory $errbotPath
