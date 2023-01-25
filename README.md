# StockBot

StockBot is a python code that can be scheduled using crontab to automatically send a text message 
to the user when the market closes with information on how much they have in a particular stock. 

## Requirements
- Python 3
- Twilio Credentials
- Selenium
- Chrome & Chromedriver

## Setup 
The user is required to:
- Set up their own crontab scheduling based on their timezone (e.g. "0 13 * * 1-5 /bin/bash/python3 /path/to/stockbot.py" for Pacific Standard Time)
- Set up a Twilio messaging account
- Switch the url variable to the google search url of their stock
- Set the shares_owned variable to the amount of shares they own

## Note
Please make sure to replace the placeholders in the code with your own information
