import os
from twilio.rest import Client

def send_whatsapp_message(to_number, message_body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_whatsapp_number = os.getenv('TWILIO_WHATSAPP_FROM')
    
    # Twilio WhatsApp numbers must be in the format 'whatsapp:+1234567890'
    if not to_number.startswith('whatsapp:'):
        to_number = f'whatsapp:{to_number}'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=to_number
    )
    return message.sid
