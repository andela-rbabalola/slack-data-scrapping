[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# OPEN-Andela Slack Team Data Scraping
Analysis of data from scrapping OPEN-Andela

## About
This is a Python 3 Demo Project built using the `SlackCLient` python package to get information from the OPEN-Andela Channel.
Make sure this is only run in a Python3 Envrionment.

## Installation
Be sure to install the requirements in your virtual environment by running the command: `pip install -r requirements.txt`.
This installs the required packages to run the python scripts here.

Once this is done, create a `.env` file to house your environment variables. The only variable needed here is a token for accessing the slack team.
Example:
`SLACK_TOKEN=hfbdscnkhbhdjscnacvsadc`

## How To Use
Running the `slack_scrapper.py` script with the command `python slack_scrapper.py` does the following:
  - Saves the list of channels on OPEN-Andela to a `channels.txt` file.
  - Save user details to a `user.txt` file.
  - Post a message to the `api_test` channel.
  - Retrieve all message from the default channel(#api_test) or pass the channel ID as an argument. e.g `python slack_scrapper.py C3662H51`

## Contributors
- **Rotimi Babalola**
- **Olajide Bolaji 'Nuel**
- **Inumidun Amao**
