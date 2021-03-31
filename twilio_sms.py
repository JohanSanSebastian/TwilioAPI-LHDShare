# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello World!!! This message was sent by an automated bot made by Johan Sebastian to remind you to join LHD Share", # Part that sends the SMS
                    from_='',
                    to=''
                )

print(message.sid)
