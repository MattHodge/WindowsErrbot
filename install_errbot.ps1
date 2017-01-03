# Add Paths
$env:Path += ";C:\Program Files\Git\bin\;C:\Python35"

# Install Choco
if (!(Get-Command -Name 'choco'))
{
    $env:chocolateyUseWindowsCompression = 'true'
    iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
}

# Install python
if (!(Get-Command -Name 'python' -ErrorAction SilentlyContinue))
{
    choco install python -version 3.5.2.20161029 -y
}

# Install Git
if (!(Get-Command -Name 'git' -ErrorAction SilentlyContinue))
{
    choco install git.install -y
}

# Install Required Python Packages
& python -m pip install --upgrade pip
& python -m pip install err
& python -m pip install slackclient
& python -m pip install git+https://github.com/alvaroaleman/pywinrm.git@bugfix/python3_stderr#egg=pywinrm

# Create Errbot Directories
New-Item -Type Directory -Path 'C:\errdata' -Force
