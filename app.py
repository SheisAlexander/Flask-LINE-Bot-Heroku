import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("JkZaTtcMTsoCanb1d/AWJY8IZBRiEdwv97RZNk8XHAIL8G1kN8ApU0tDnALAMH8JX+Qmzw2W6XOqDmKsC6xWfZYvV1Oh2fEEtr1/bcq4Wfa1D6QKV1eHFpnfRvrQg8HqIt0LhgVJuTJl2YuTXBJ2sgdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET7add63e473300955478e32d167e2fb11"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
