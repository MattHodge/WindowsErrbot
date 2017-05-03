Describe "Demo" {
    Context "Vagrant" {
        It "errbot should exist" {
            Test-Path "C:\errbot" | Should Be $true
        }
        It "errbot folder contains files" {
            $items = Get-ChildItem -Path "C:\errbot"
            $items.Count | Should BeGreaterThan 8
        }
        It "has slack token in environment variables" {
            $env:slack_api_key -like "xoxb*" | Should Be $true
        }
    }
    Context "Installation" {
        It "git should be installed" {
            (get-command git).Name | Should Match "git.exe"
        }
        It "python should be installed" {
            (get-command python).Name | Should Match "python.exe"
        }
        It "python exe should exist" {
            (get-command python).Source | Test-Path | Should Be $true
        }
        # It "nssm should be installed" {
        #     (get-command nssm).Name | Should Match "nssm.exe"
        # }

        $pipPackages = & python -m pip freeze

        It "pip packages installed" {
            $pipPackages.Count | Should Be 37
        }
        It "pip pywinrm installed" {
            $pipPackages -contains "pywinrm==0.2.0" | Should Be $true
        }
        It "errbot event log source exists" {
            [system.diagnostics.eventlog]::SourceExists('Errbot') | Should Be $true
        }
    }
}
