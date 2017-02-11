$WUSettings = (New-Object -com 'Microsoft.Update.AutoUpdate').Settings
$WUSettings.NotificationLevel = 1
$WUSettings.save()

Set-Item WSMan:\\localhost\\Client\\TrustedHosts * -Force
