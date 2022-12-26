from asyncio import events
import os
from xml.sax.handler import feature_external_ges
import requests

from linebot import LineBotApi
from linebot.models import *
from flask import Flask, request, jsonify, abort, send_file

#  載入環境變數
from dotenv import load_dotenv
load_dotenv()

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)


def send_text_message(reply_token, text):
    if text is not None:
        line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(id, img_url):
    img = ImageSendMessage(
        preview_image_url = img_url,
        original_content_url= img_url
    )
    line_bot_api.push_message(id, img)

    return "OK"

def push_message(id, msg):
    line_bot_api.push_message(id, TextSendMessage(text=msg))

    return "OK"

def send_button_template(reply_token, url, theme, name, description):
    buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url=theme, # 主題背景
            title=name,
            text=description, # 不能再長了
            actions=[
                # 最多四個按鈕
                # PostbackAction( 
                #     label='偷偷傳資料',
                #     display_text='檯面上',
                #     data='action=檯面下'
                # ),
                # MessageAction(
                #     label='光明正大傳資料',
                #     text='我就是資料'
                # ),
                URIAction(
                    label='View more',
                    uri=url
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template_message)

def push_button_template(id, url, theme, name, description):
    buttons_template_message = TemplateSendMessage(
        alt_text='這個看不到',
        template=ButtonsTemplate(
            thumbnail_image_url=theme, # 主題背景
            title=name,
            text=description, # 不能再長了
            actions=[
                # 最多四個按鈕
                # PostbackAction( 
                #     label='偷偷傳資料',
                #     display_text='檯面上',
                #     data='action=檯面下'
                # ),
                # MessageAction(
                #     label='光明正大傳資料',
                #     text='我就是資料'
                # ),
                URIAction(
                    label='View more',
                    uri=url
                )
            ]
        )
    )
    line_bot_api.push_message(id, buttons_template_message)

def send_flex_message(reply_token, content): # no use 
    flex_message = FlexSendMessage(
        alt = 'Recommandation',
        contents = content
    )
    line_bot_api.reply_message(reply_token, flex_message)

    return "OK"

def push_flex_message(id, content): # no use
    flex_message = FlexSendMessage(
        alt = 'Recommandation',
        contents = content
    )
    line_bot_api.push_message(id, flex_message)

    return "OK"
"""
def send_button_message(id, text, buttons):
    pass
"""