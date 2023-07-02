from twilio.rest import Client

# Twilio account credentials
# your account_sid and auth_token
account_sid = "your account_sid" 
auth_token = "your auth_token"
client = Client(account_sid, auth_token)

# Define a dictionary of phone numbers and messages
messages = {
    '+91123456789': 'This is a test message.'
}

# Iterate over the dictionary and send messages
for number, message in messages.items():
    try:
        message = client.messages.create(
            body=message,
            from_='+1499999999',
            to=number
        )
        print(f"Message sent to {number} successfully. Message SID: {message.sid}")
    except Exception as e:
        print(f"Error sending message to {number}: {str(e)}")
