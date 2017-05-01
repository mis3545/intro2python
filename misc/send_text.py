from twilio.rest import TwilioRestClient

# Your Account SID from www.twilio.com/console
account_sid = "Your Account SID from www.twilio.com/console"
# Your Auth Token from www.twilio.com/console
auth_token = "Your Auth Token from www.twilio.com/console"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Zhi Li",
                                 to="+1##########",    # Replace with your phone number
                                 from_="+1##########")  # Replace with your Twilio number

print(message.sid)
