# Wakatime-Leaderboards📶
[![Wakatime Leaderboards](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/wakatime.yml/badge.svg)](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/wakatime.yml)
[![Release](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/release.yml/badge.svg)](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/release.yml)
[![Bandit](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/bandit.yml/badge.svg)](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/bandit.yml)
[![CodeQL & Pylint](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/codeql.yml/badge.svg)](https://github.com/Nicconike/Wakatime-Leaderboards/actions/workflows/codeql.yml)
[![codecov](https://codecov.io/gh/Nicconike/Wakatime-Leaderboards/graph/badge.svg?token=CX701AOW5Y)](https://codecov.io/gh/Nicconike/Wakatime-Leaderboards)
![Docker Image Size](https://img.shields.io/docker/image-size/nicconike/wakatime-leaderboards?logo=docker&label=Docker%20Image)
![Docker Pulls](https://img.shields.io/docker/pulls/nicconike/wakatime-leaderboards?logo=docker&label=Docker%20Pulls)
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fgithub.com%2FNicconike%2FWakatime-Leaderboards%2Fblob%2Fmaster%2Fpyproject.toml%3Fraw%3Dtrue)
![Pylint](https://img.shields.io/badge/Pylint-9.08-darkgreen?logo=python)
![GitHub License](https://img.shields.io/github/license/nicconike/Wakatime-Leaderboards)
[![Visitor Badge](https://badges.pufler.dev/visits/nicconike/Wakatime-Leaderboards)](https://badges.pufler.dev)

> ### Automated WakaTime leaderboards for your GitHub profile

***
## Prerequisites
1. **Wakatime API Key:** API key is required to fetch your account details. Get your API key from [here](https://wakatime.com/api-key).
2. **Markdown Comments:** Update the markdown file by adding the comments where your Wakatime Leaderboard Stats will be embedded to. Refer [here](#Update-Readme) to learn more.

> [!NOTE]
> **Coding Activity:** Total hours coded over the last 7 days from Yesterday, using default 15 minute timeout, only shows coding activity from known languages.
>
> **Public Leaderboards:** You will appear in the public leaderboards only if your weekly coded hours is around 10 hrs(Changes from time to time).

***
## Example
<!-- Wakatime-Start -->
### Wakatime Leaderboards (Worldwide)

#### Public Leaderboards (Weekly)

| Ranked | Hours Coded | Daily Avg |
| ------ | ----------- | --------- |
| 9650 | 11 hrs 36 mins | 1 hrs 39 mins |

#### Country Leaderboard (India)

| Ranked | Hours Coded | Daily Avg |
| ------ | ----------- | --------- |
| 9650 | 11 hrs 36 mins | 1 hrs 39 mins |

#### Top Language (Python)

| Ranked | Hours Coded | Daily Avg |
| ------ | ----------- | --------- |
| 1981 | 2 hrs 45 mins | 23 mins |


<!-- Wakatime-End -->
***
## Update README
Add below comment in your markdown file for Wakatime Leaderboards Stats
```md
<!-- Wakatime-Start -->
<!-- Wakatime-End -->
```
***
## Setup with Example
After completing the steps mentioned in the [Prerequisites](#Prerequisites), you have to save all the mentioned keys(except markdown comments) like Wakatime API Key as Secrets in your Github repo's settings.

> Repo Settings -> Security -> Secrets and Variables -> Actions -> Add in Repository Secrets

If you are new to **Github Secrets** then you can checkout this official doc [here](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

**Sample Workflow File**

`wakatime.yml`

```yaml
name: Wakatime Leaderboards

on:
    schedule:
        # Runs every Monday at 12AM IST (UTC+5:30)
        - cron: "30 18 * * 0"
    workflow_dispatch:
    push:
        branches: master

jobs:
    update-readme:
        name: Wakatime Leaderboards
        runs-on: ubuntu-latest
        steps:
          - name: Run Wakatime Leaderboards
            uses: nicconike/wakatime-leaderboards@master
            env:
                WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
```
***
## Contributions

Star⭐ and Fork🍴 the Repo to start with your feature request(or bug) and experiment with the project to implement whatever Idea you might have and sent the Pull Request through 🤙

Please refer [Contributing.md](https://github.com/Nicconike/Wakatime-Leaderboards/blob/master/.github/CONTRIBUTING.md) to get to know how to contribute to this project.
And thank you for considering to contribute.
***
