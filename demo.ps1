# BEFORE DEMO
# connect to RDP sessions

# validate !dscfeature telnet-client 172.28.128.101

###########################
# DEMO 1
###########################

# MAC
# Get Slack API Token from Slack Client

# VM
# Set the slack_api_key environment variable

# MAC
code start_errbot.ps1

# VM
cd C:\errbot
.\start_errbot

# SLACK
# Watch calculon appear online
/open demo30
/invite @calculon
!help

###########################
# DEMO 2
###########################

# SLACK
!help hello
!hello

# MAC
code hello.py
# Explain def hello

# SLACK
!saymyname matt

# MAC
code hello.py
# Explain def saymyname

###########################
# DEMO 3
###########################
# SLACK
!hellopretty

# MAC
code hello.py
# explain def hellopretty

###########################
# DEMO 4
###########################
# SLACK
!getdate

# MAC
code psexample.py
# explain run_ps_inline and run_ps_function_file

# SLACK
!getlastboot

# MAC
code psexample.py
# explain getlastboot

# SLACK
!getsvc bits
!getsvc spooler

# MAC
code psexample.py
# explain getsvc
code Get-ServiceBot.ps1

# SLACK
!getsvc fake

# MAC
code Get-ServiceBot.ps1
# uncomment error handling

# SLACK
!getsvc fake

###########################
# DEMO 5
###########################

# SLACK
!stopsvc bits 172.28.128.101
!startsvc bits 172.28.128.101
!startsvc fake 172.28.128.101

# MAC
code psremote.py
# explain run_remote_ps, stopsvc, startsvc

# SLACK
!dscfeature telnet-client 172.28.128.101
!dscfeature telnet-client 172.28.128.101 --ensure absent
!dscfeature web-server 172.28.128.101

# MAC
code psremote.py
# explain dscfeature
# load http://localhost:8080

###########################
# DEMO 6
###########################
# SLACK
!getkey

# MAC
code secrets.py

# VM
# Add a generic password in the network credential on Errbot VM as demo and username

# SLACK
!getkey

# Auditing commands
# MAC
code psexample.py
# Uncomment logging to the eventviewer

# SLACK
!plugin reload psexample # in PM
!getsvc bits

# VM
# look at event log

# Access control
code config.py
# uncomment access control

# SLACK
!restart
!getsvc bits
