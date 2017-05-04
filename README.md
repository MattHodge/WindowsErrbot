# WindowsErrbot

This repository makes it easy to get an Errbot development environment running on Windows.

<!-- TOC depthFrom:2 -->

- [Vagrant](#vagrant)
    - [Create an .env.yml file](#create-an-envyml-file)
- [Manual Setup](#manual-setup)

<!-- /TOC -->

## Vagrant
### Create an .env.yml file

To prevent secrets getting checked into the repo, create a `.env.yml` file in the root of the repo.

It should look like the following:

```yml
---
configs:
    slack_api_key: xoxb-xxxxx-xxYourAPIKeyxx
```

Any `configs` that are added will automatically be added to the `Machine` level environment variable of the Vagrant box.

## Manual Setup

If you want to setup Errbot on an existing Windows machine, you can:

* Run `install_errbot.ps1`
* Make `C:\errbot` directory and copy in `config.py` and `config_slack.py`
* Make `C:\errbot\plugins` directory
