# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('pF0h1aBXENILkjJvouN8+A+bSy357OiO0rJLhDw2921tgZRczjAns+VRSrrVOuZJjW4+sLNErqXslosz5K7/9sSdil97gw6ccFClDEw3oCr6HAsCVxZuCbma0VYuWsOTXcUTZ26NiCCaJXInYYBJGwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e640f83e4152426c14345617165a23d8')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    msg = event.message.text
    if 'joyce' in msg:
        message = TextSendMessage(text='生日: 1995/02/03\n手機: 0973019023')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'LeetCode' in msg:
        message = TextSendMessage(text='https://leetcode.com/problemset/all/')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'udemy' in msg:
        message = TextSendMessage(text='https://www.udemy.com/')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'studio' in msg:
        message = TextSendMessage(text='http://www.studioclassroom.com/')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'learnc' in msg:
        message = TextSendMessage(text='https://www.youtube.com/c/KenYiLee')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'github' in msg:
        message = TextSendMessage(text='https://github.com/')
        line_bot_api.reply_message(event.reply_token, message)
    elif 'list' in msg:
        message = TextSendMessage(text='You can input : \njoyce\nLeetCode\nudemy\nstudio\nlearnc\ngithub')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()