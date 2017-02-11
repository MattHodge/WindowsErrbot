<#
.Synopsis
   Gets a service in bot format
#>
function Get-ServiceBot
{
    [CmdletBinding()]
    Param
    (
        # Param1 help description
        [Parameter(Mandatory=$true)]
        $Name
    )

    $svc = Get-Service -Name $name

    Write-Output "Service *$($svc.DisplayName)* (``$($svc.Name)``) is currently ``$($svc.Status)``"
}
