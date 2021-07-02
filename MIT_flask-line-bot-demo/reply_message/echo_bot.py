import os
import csv
from datetime import datetime
if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or 'YOUR_SECRET'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_ACCESS_TOKEN'

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# Echo function
# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text)
#     )

# CSV Example
# import csv
# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     rows_list = []
#     with open(os.path.abspath("maskdata.csv"), newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         for row in rows:
#             rows_list.append(row)
#
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=str(rows_list[1]))
#     )

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    #if shemar, save to shemardata.csv
    #request NHI number and match it to patient then if 
    #visualisation
    with open('patient_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(datetime.today().strftime('%Y-%m-%d') + ',' + event.message.text)
        #append date to data for graph
        #append 2 datas and reply
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="your fada head shanyqua")
    )
 
    
#store message in csv file with row
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
