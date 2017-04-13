$WUSettings = (New-Object -com 'Microsoft.Update.AutoUpdate').Settings
$WUSettings.NotificationLevel = 1
$WUSettings.save()

Set-Item WSMan:\\localhost\\Client\\TrustedHosts * -Force

# Enable RDP
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1
