<#
.Synopsis
   Gets a service in bot format
#>
function Get-ServiceBot
{
    [CmdletBinding()]
    Param
    (
        # Name of the service
        [Parameter(Mandatory=$true)]
        $Name
    )

    $svc = Get-Service -Name $name

    Write-Output "Service *$($svc.DisplayName)* (``$($svc.Name)``) is currently ``$($svc.Status)``"

    <# Error Handling

    $ErrorActionPreference = 'Stop'

    try
    {
        $svc = Get-Service -Name $name

        Write-Output "Service *$($svc.DisplayName)* (``$($svc.Name)``) is currently ``$($svc.Status)``"
    }
    catch
    {
        Write-Output ":fire: Service ``$($Name)`` does not exist on this machine."
    }
    #>
}
