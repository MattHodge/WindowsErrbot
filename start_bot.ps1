Param
(
    # Type of start mode for errbot
    [Parameter(Mandatory=$true)]
    [ValidateSet("text", "slack")]
    $mode
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

if ($mode -eq 'text')
{
    C:\Python35\Scripts\errbot.exe -c .\config_slack.py
}
else
{
    C:\Python35\Scripts\errbot.exe -c .\config_slack.py
}
