from twilio.rest import Client

account_sid = 'AC506d30f98339e438061ee60e2d79ebe2'
auth_token = '70b435c6b7c8fcaf321711412db40df0'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Your new password - ', to='+375296305338', from_="+18043312662")

print(message)
