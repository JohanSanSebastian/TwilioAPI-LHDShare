# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>Hello There Welcome to LHD Share</Say></Response>', # Automated voice
    to='',
    from_=''
)

print(call.sid)
