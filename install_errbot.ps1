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

# Install python
if (!(Get-Command -Name 'python' -ErrorAction SilentlyContinue))
{
    choco install python -version 3.5.2.20161029 -y
}
else
{
    Write-Output "Python is already installed"
}

# Install Git
if (!(Get-Command -Name 'git' -ErrorAction SilentlyContinue))
{
    choco install git.install -y
}
else
{
    Write-Output "Git is already installed"
}

# Install Required Python Packages
& python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

# Create Errbot Directories
New-Item -Type Directory -Path 'C:\vagrant\data' -Force
