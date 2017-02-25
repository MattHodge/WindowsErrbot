$errbotExePath = (Get-Command errbot).Source
$errbotPath = "C:\errbot"
$serviceName = 'errbot'

if (Get-Service -Name $serviceName -ErrorAction SilentlyContinue)
{
    Stop-Service -Name $serviceName -Force
    & nssm remove $serviceName confirm
}

& nssm install $serviceName $errbotExePath -c config.py
& nssm set $serviceName AppDirectory $errbotPath

Start-Service -Name $serviceName
