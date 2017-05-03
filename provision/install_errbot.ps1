$botPath = "C:\errbot"

cd $botPath

# Add Paths
$env:Path += ";C:\Program Files\Git\bin\;C:\Python35"

# Install Choco
if (!(Get-Command -Name 'choco'))
{
    $env:chocolateyUseWindowsCompression = 'true'
    iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
}
else
{
    Write-Output "Chocolatey is already installed"
}

choco install python -version 3.5.2.20161029 -y
choco install git.install -y

# used for running Errbot as a Service
# choco install nssm -y

# used for demo purposes
# choco install visualstudiocode -y

# Install Required Python Packages
python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

# Create Errbot Directories
New-Item -Type Directory -Path "$($botPath)\data" -Force

# Create Eventlog source for auditing (not required)
if ([system.diagnostics.eventlog]::SourceExists('Errbot'))
{
    Write-Output "Event source for Errbot Already Exists"
} else {
    [system.diagnostics.EventLog]::CreateEventSource('Errbot', 'Application')
}

# used for validating the demo setup
choco install pester -y

# run tests
. $botPath\provision\demo.tests.ps1
