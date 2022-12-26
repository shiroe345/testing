# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
客製化選單FlexSendMessage
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('AgLy/KtLPrFL0n7Wj+g9rZ74rrIS370SJKjurMFIE2W0z3oXw+9fmYqY28o3WKcxYKcsa8pSFXkyh14pJBHSY6wJFm6v3UqYw69S5NCDSJAU+7FML+jYjlLgVpA0t6l/oKfqIv1gE1Vm6Sf9d+7gwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('98755333a647489c27736689a004154d')



# 監聽所有來自 /callback 的 Post Request
@app.route("/abc", methods=['POST'])
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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('告訴我秘密',message):
        # Flex Message Simulator網頁：https://developers.line.biz/console/fx/
        flex_message = FlexSendMessage(
            alt_text='行銷搬進大程式',
            contents={
  "type": "bubble",
  "hero": {
    "type": "image",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "url": "https://i.im.ge/2022/12/25/q3Uow6.usd-sway-four.png"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://linecorp.com"
    },
    "contents": [
      {
        "type": "text",
        "text": "USD Sway 4",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "text",
                "text": "$199",
                "weight": "bold",
                "margin": "sm",
                "flex": 0
              },
              {
                "type": "text",
                "text": "dollars",
                "size": "sm",
                "align": "end",
                "color": "#aaaaaa"
              }
            ]
          }
        ]
      },
      {
        "type": "text",
        "text": "Model Year 2020",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      },
      {
        "type": "text",
        "text": "Skate Type Aggressive",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      },
      {
        "type": "text",
        "text": "Skill Level  Beginner and Better",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      },
      {
        "type": "text",
        "text": "Weight\t1740g (US 8.0 EU 41)",
        "wrap": True,
        "color": "#aaaaaa",
        "size": "xxs"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "margin": "xxl",
        "action": {
          "type": "uri",
          "label": "View more",
          "uri": "https://www.inlinewarehouse.com/USD_Sway_Team_IV/descpage-710173.html"
        }
      }
    ]
  }
}
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
