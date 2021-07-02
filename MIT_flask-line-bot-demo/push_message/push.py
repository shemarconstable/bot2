import os

from linebot.models import TextSendMessage

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys
from linebot import LineBotApi

channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'QeNDzovLdlZSMyJR/lj0bqT/ON2ZXFzeWZCfaA9syt2SoLEjxoXnNOd02BOKdWF/RyBdNzB7WQltroEgCRRNCH3d19+u05m+0mAtC28MI41D3gIMoHKF7Tbz5g28rOuoBQzTU2npHfZDVNxCrV51oAdB04t89/1O/w1cDnyilFU='
print(channel_access_token)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#push_messageself-to-messages-notification_disabledfalse-timeoutnone
# Document: https://developers.line.biz/en/reference/messaging-api/#send-push-message

e1 = ['U1cf6a488e538c3e7f0c06fc5ea3e7b46', 'U1818a4f985d38153e06612fc32dc11bc', 'U6c2d0dd3e2053f1dfc50f66e95dfbda4']
for i in e1:
    line_bot_api.push_message(i, TextSendMessage(text='ALERT!!! \n Hello emergency contact of Shemar, Please be advised that Shemar has an EMERGENCY and the medical personel are currently on their way to his location'))

