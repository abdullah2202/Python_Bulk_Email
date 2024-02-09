# Bulk Send Email via Python

## Description

This script will send an email to each row from an excel sheet. You can insert any other column from the excel sheet into the email. This can be useful when sending unique links or codes to a list of recipients.

## Configuration

Any login data for the email system is stored in the JSON file. An example is provided to show what data is needed. I might add more fields in the future if needed.

### Issues with Gmail

I have only used this with a Google Workspace GMail account. If 2FA is enabled on your account, as it should be, you will need to create an **app password** and use that for this application, otherwise you can use your normal Username and Password after enabling **Less Secure Apps**

## Installation

Install any required modules using `pip install -r requirements.txt` 

## Usage

Have the Data Excel sheet in the same folder and configuration JSON set accordingly. Run **bulk_email.py** 

You can run a test by having test data in the excel sheet first. This will ensure the emails are working via this method.
