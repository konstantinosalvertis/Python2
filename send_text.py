from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC695595632f22a06337abc7b01d306a6e"
# Your Auth Token from twilio.com/console
auth_token  = "b78bd556bc82598ffedd7cae85925095"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+xxx", 
    from_="+16267885784",
    body="My name is Musk!")

print(message.sid)
