from flask import Flask, request, abort
from bs4 import BeautifulSoup
from botFunction import *
from linebot import (
    LineBotApi
)
from webhook2 import WebhookHandler
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    actions, __init__, responses, sources, base, flex_message, messages, rich_menu, template, error, imagemap, send_messages
)
from events import *
from linebot.models.send_messages import *
import time
import datetime
app = Flask(__name__)
#tmpToken=""
# Channel Access Token
line_bot_api = LineBotApi('t5Og/yNaTFE+Wwn201Gkie5j/PyNb07l5V8cW5OPNAH8vIySJQMzD04gelrtZzbXyM1j/f83E7g5C2ummlyXiEimqzJlqDOFVLSAcoZvwJ/Hr4tR+SBZhhX147wYnUPapCqqd3Y2dLc8YqS09Y9gLAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('44d2b8341262f02d6cac5545e6915577')

# Channel Access Token
#line_bot_api2 = LineBotApi('5MtHcL/AVUfJFWgndIPwgs035d8XwKMxqYekxm/YxYZ+mlVHMmkC6E3vtZCNmMIgKZee8LW7y6dj8/W6z4SYhZtWTiiFePFaI+Jp3mfig0V81f2leJSHjL9qhYiS7NqtsBQkQ6BF6Tc0TyWrL23wBAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
#handler2 = WebhookHandler('d06fdd69083728dc538bffa94a0edc89')



# 監聽所有來自 /callback 的 Post Request
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


@handler.add(MemberJoinEvent)
def handle_memberJoined(event):
    #global tmpToken
    #tmpToken = event.reply_token
    #newMember = line_bot_api.get_profile(event.source.user_id)
    #profile = line_bot_api.get_profile(event.source.user_id)
    message=TextMessage(text="歡迎加入劉萱63醫師諮詢，新來的朋友們請去記事本五月那篇留下Twitch ID與暱稱^^")
    line_bot_api.reply_message(event.reply_token, message)

#@handler.add(MemberLeaveEvent)
#def handle_memberLeft(event):
    #line_bot_api.reply_message(event.reply_token, TextMessage(text=event.type))
    #global tmpToken
    #tmpToken = event.reply_token
    #line_bot_api.reply_message(tmpToken, TextSendMessage(text=event.type))
    #line_bot_api.push_message("C4fe2e6fd176c7822ed60a78d3941aaea", TextSendMessage(text=str(tmpToken)))



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):   
    adminID=["Ue302eb57af67d978f3a5c12055577d55"]

    if event.message.text=="!GID":           
        message = TextSendMessage(text=event.source.group_id)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!RID":                  
        message = TextSendMessage(text=event.source.room_id)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!UID":                  
        message = TextSendMessage(text=event.source.user_id)
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text=="!test" and event.source.user_id in adminID:           
        message = TextSendMessage(text="測試權限成功")
        line_bot_api.reply_message(event.reply_token, message)

    


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
    #ssl_context='adhoc'
