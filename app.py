from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('MmwqAimfy08ghbG8weaNJvmufqpUzQ5tXMMS7XWSaI+TCba3V00lqWucGf4h825hvq/8oZ8qsW8w9MVyt6tsmkzXg4G+1/O+1JJU51gRqofGKWeLyuHTXnEFQ8WqNlMzuUBW8eu5l6fBxX+vkeJuoAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('634f4b244942250a45adda99aafd9abf')

# /callback の Post Request
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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    app.logger.info("Message: " + message)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="やほー！今、蝶々を取りに行ってるよ！後で、メッセージしてみてね！"))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
